import argparse
from pathlib import Path

import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


def to_bool_value(x):
    if isinstance(x, bool):
        return x
    return str(x).lower() in ["true", "1", "yes"]


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input",
        default="outputs/switching_facts_controlled_qa_base_v4_strict.csv",
        help="Switching facts CSV from the final strict setup.",
    )

    parser.add_argument(
        "--output",
        default="outputs/hidden_states_switching_controlled_qa_base_v4_strict.pt",
        help="Output .pt file containing hidden-state activations.",
    )

    parser.add_argument(
        "--metadata-output",
        default="reports/controlled_qa_base_v4_strict/hidden_states_metadata_controlled_qa_base_v4_strict.csv",
        help="CSV output with metadata for the extracted hidden states.",
    )

    parser.add_argument(
        "--model",
        default="google/gemma-2-2b",
        help="Model name. This should match the model used in the final experiment.",
    )

    parser.add_argument(
        "--layers",
        default="6,9,12",
        help="Comma-separated layer indices to extract.",
    )

    args = parser.parse_args()

    layers = [int(x.strip()) for x in args.layers.split(",")]

    df = pd.read_csv(args.input)

    print("Rows:", len(df))
    print("Facts:", df["fact_id"].nunique())
    print("Layers:", layers)
    print("CUDA available:", torch.cuda.is_available())
    print("GPU:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "no GPU")

    if not torch.cuda.is_available():
        raise RuntimeError("CUDA is not available. This script is intended to run on a GPU node.")

    tokenizer = AutoTokenizer.from_pretrained(args.model)

    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        torch_dtype=torch.float16,
        device_map="auto",
    )
    model.eval()

    activation_rows = []
    metadata_rows = []

    for i, row in df.iterrows():
        question = row["question"]
        is_correct = to_bool_value(row["is_correct"])

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

            activation_rows.append(
                {
                    "fact_id": row["fact_id"],
                    "variant_id": row["variant_id"],
                    "layer": layer,
                    "is_correct": is_correct,
                    "last_token_activation": last_token_activation,
                    "mean_prompt_activation": mean_prompt_activation,
                }
            )

            metadata_rows.append(
                {
                    "fact_id": row["fact_id"],
                    "variant_id": row["variant_id"],
                    "layer": layer,
                    "is_correct": is_correct,
                    "question": question,
                    "correct_answer": row["correct_answer"],
                    "generated_answer": row.get("generated_answer", ""),
                    "n_tokens": len(tokens),
                    "tokens": " | ".join(tokens),
                }
            )

        print(f"[{i + 1}/{len(df)}] done: {row['fact_id']} {row['variant_id']}")

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.metadata_output).parent.mkdir(parents=True, exist_ok=True)

    torch.save(activation_rows, args.output)
    pd.DataFrame(metadata_rows).to_csv(args.metadata_output, index=False)

    print()
    print("Saved activations:", args.output)
    print("Saved metadata:", args.metadata_output)
    print("Activation rows:", len(activation_rows))


if __name__ == "__main__":
    main()
