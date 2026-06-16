import argparse
import ast
import re
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


def normalize_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def parse_possible_answers(value, correct_answer):
    answers = []

    if pd.notna(correct_answer):
        answers.append(str(correct_answer))

    if pd.isna(value):
        return answers

    value = str(value)

    try:
        parsed = ast.literal_eval(value)
        if isinstance(parsed, list):
            answers.extend([str(x) for x in parsed])
        else:
            answers.append(str(parsed))
    except Exception:
        answers.append(value)

    clean_answers = []
    seen = set()

    for ans in answers:
        ans = ans.strip()
        if ans and ans not in seen:
            clean_answers.append(ans)
            seen.add(ans)

    return clean_answers


def is_correct_answer(generated_answer, answer_aliases):
    generated_norm = normalize_text(generated_answer)

    for ans in answer_aliases:
        ans_norm = normalize_text(ans)
        if ans_norm and ans_norm in generated_norm:
            return True

    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/prompt_variants.csv")
    parser.add_argument("--output", default="outputs/prompt_outputs_v1.csv")
    parser.add_argument("--model", default="google/gemma-2-2b-it")
    parser.add_argument("--max-new-tokens", type=int, default=40)
    args = parser.parse_args()

    print("CUDA available:", torch.cuda.is_available())
    if torch.cuda.is_available():
        print("GPU:", torch.cuda.get_device_name(0))

    df = pd.read_csv(args.input)

    tokenizer = AutoTokenizer.from_pretrained(args.model)

    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        dtype=torch.float16,
        device_map="cuda",
    )

    rows = []

    for i, row in df.iterrows():
        question = row["question"]
        correct_answer = row["correct_answer"]
        possible_answers = row.get("possible_answers", "")

        answer_aliases = parse_possible_answers(possible_answers, correct_answer)

        inputs = tokenizer(question, return_tensors="pt").to("cuda")
        input_len = inputs["input_ids"].shape[-1]

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=args.max_new_tokens,
                do_sample=False,
                pad_token_id=tokenizer.eos_token_id,
            )

        generated_only_ids = outputs[0][input_len:]
        generated_answer = tokenizer.decode(
            generated_only_ids,
            skip_special_tokens=True,
        ).strip()

        full_output = tokenizer.decode(
            outputs[0],
            skip_special_tokens=True,
        ).strip()

        correct = is_correct_answer(generated_answer, answer_aliases)

        print("=" * 80)
        print(f"row: {i + 1}/{len(df)}")
        print("fact_id:", row["fact_id"])
        print("variant_id:", row["variant_id"])
        print("question:", question)
        print("generated:", generated_answer)
        print("correct_answer:", correct_answer)
        print("answer_aliases:", answer_aliases[:5])
        print("is_correct:", correct)

        rows.append({
            "fact_id": row["fact_id"],
            "variant_id": row["variant_id"],
            "question": question,
            "original_question": row.get("original_question", ""),
            "correct_answer": correct_answer,
            "possible_answers": possible_answers,
            "type": row.get("type", ""),
            "generated_answer": generated_answer,
            "full_output": full_output,
            "is_correct": correct,
        })

    out_df = pd.DataFrame(rows)
    out_df.to_csv(args.output, index=False)
    print(f"\nSaved outputs to {args.output}")


if __name__ == "__main__":
    main()
