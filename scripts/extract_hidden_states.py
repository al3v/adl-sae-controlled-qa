import argparse
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="outputs/switching_facts_v1.csv")
    parser.add_argument("--output", default="outputs/hidden_states_switching_v1.pt")
    parser.add_argument("--metadata-output", default="reports/hidden_states_metadata_v1.csv")
    parser.add_argument("--model", default="google/gemma-2-2b-it")
    parser.add_argument("--layers", default="6,9,12")
    args = parser.parse_args()

    layers = [int(x.strip()) for x in args.layers.split(",")]

    df = pd.read_csv(args.input)

    print("Rows:", len(df))
    print("Facts:", df["fact_id"].nunique())
    print("Layers:", layers)
    print("CUDA available:", torch.cuda.is_available())
    print("GPU:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "no gpu")

    tokenizer = AutoTokenizer.from_pretrained(args.model)

    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        dtype=torch.float16,
        device_map="cuda",
    )
    model.eval()

    activation_rows = []
    metadata_rows = []

    for i, row in df.iterrows():
        question = row["question"]

        inputs = tokenizer(question, return_tensors="pt").to("cuda")

        with torch.no_grad():
            out = model(
                **inputs,
                output_hidden_states=True,
                use_cache=False,
            )

        input_ids = inputs["input_ids"][0].detach().cpu()
        tokens = tokenizer.convert_ids_to_tokens(input_ids)

        last_token_index = inputs["input_ids"].shape[1] - 1

        for layer in layers:
            hidden = out.hidden_states[layer][0]

            last_token_activation = hidden[last_token_index].detach().cpu().float()
            mean_prompt_activation = hidden.mean(dim=0).detach().cpu().float()

            activation_rows.append({
                "fact_id": row["fact_id"],
                "variant_id": row["variant_id"],
                "layer": layer,
                "is_correct": bool(row["is_correct"]),
                "last_token_activation": last_token_activation,
                "mean_prompt_activation": mean_prompt_activation,
            })

            metadata_rows.append({
                "fact_id": row["fact_id"],
                "variant_id": row["variant_id"],
                "layer": layer,
                "is_correct": bool(row["is_correct"]),
                "question": question,
                "correct_answer": row["correct_answer"],
                "generated_answer": row["generated_answer"],
                "n_tokens": len(tokens),
                "tokens": " | ".join(tokens),
            })

        print(f"[{i+1}/{len(df)}] done: {row['fact_id']} {row['variant_id']}")

    torch.save(activation_rows, args.output)
    pd.DataFrame(metadata_rows).to_csv(args.metadata_output, index=False)

    print()
    print("Saved activations:", args.output)
    print("Saved metadata:", args.metadata_output)
    print("Activation rows:", len(activation_rows))


if __name__ == "__main__":
    main()
