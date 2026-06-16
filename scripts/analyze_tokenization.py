import argparse
from pathlib import Path

import pandas as pd
from transformers import AutoTokenizer


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input",
        default="outputs/switching_facts_controlled_qa_base_v4_strict.csv",
        help="Switching facts CSV from the final strict setup.",
    )

    parser.add_argument(
        "--csv-output",
        default="reports/controlled_qa_base_v4_strict/tokenization_switching_controlled_qa_base_v4_strict.csv",
        help="CSV output with tokenization details.",
    )

    parser.add_argument(
        "--md-output",
        default="reports/controlled_qa_base_v4_strict/tokenization_switching_controlled_qa_base_v4_strict.md",
        help="Markdown preview of tokenization details.",
    )

    parser.add_argument(
        "--model",
        default="google/gemma-2-2b",
        help="Tokenizer/model name. This should match the model used in the final experiment.",
    )

    args = parser.parse_args()

    df = pd.read_csv(args.input)
    tokenizer = AutoTokenizer.from_pretrained(args.model)

    rows = []

    for _, row in df.iterrows():
        question = row["question"]

        tokens = tokenizer.tokenize(question)
        token_ids = tokenizer.encode(question, add_special_tokens=True)

        rows.append(
            {
                "fact_id": row["fact_id"],
                "variant_id": row["variant_id"],
                "is_correct": row["is_correct"],
                "correct_answer": row["correct_answer"],
                "question": question,
                "n_tokens": len(tokens),
                "tokens": " | ".join(tokens),
                "token_ids": " ".join(map(str, token_ids)),
                "generated_answer": row.get("generated_answer", ""),
            }
        )

    out = pd.DataFrame(rows)

    Path(args.csv_output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.md_output).parent.mkdir(parents=True, exist_ok=True)

    out.to_csv(args.csv_output, index=False)

    with open(args.md_output, "w", encoding="utf-8") as f:
        f.write("# Tokenization analysis for switching facts\n\n")
        f.write(
            "This file shows how Gemma tokenizes prompt variants where the same fact has both correct and wrong answers.\n\n"
        )

        for fact_id, group in out.groupby("fact_id"):
            f.write(f"## {fact_id}\n\n")
            f.write(f"Correct answer: `{group['correct_answer'].iloc[0]}`\n\n")

            for _, r in group.iterrows():
                f.write(f"### Variant: {r['variant_id']}\n\n")
                f.write(f"- Correct: `{r['is_correct']}`\n")
                f.write(f"- Number of tokens: `{r['n_tokens']}`\n")
                f.write(f"- Question: {r['question']}\n")
                f.write(f"- Tokens: `{r['tokens']}`\n")
                f.write(f"- Token IDs: `{r['token_ids']}`\n")
                f.write(f"- Generated answer: {r['generated_answer']}\n\n")

    print("Saved CSV:", args.csv_output)
    print("Saved Markdown:", args.md_output)
    print("Rows:", len(out))


if __name__ == "__main__":
    main()
