import argparse
import pandas as pd


def clean_question(q):
    return str(q).strip()


def lower_first_char(q):
    return q[0].lower() + q[1:] if q else q


def double_first_space(q):
    parts = q.split(" ", 1)
    if len(parts) == 2:
        return parts[0] + "  " + parts[1]
    return q


def space_before_question_mark(q):
    q = q.strip()
    if q.endswith("?"):
        return q[:-1].rstrip() + " ?"
    return q + " ?"


def no_question_mark(q):
    q = q.strip()
    if q.endswith("?"):
        return q[:-1]
    return q


def trailing_space(q):
    return q.strip() + " "


def leading_space(q):
    return " " + q.strip()


def qa_template(q):
    return f"Question: {q}\nAnswer:"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/prompt_variants.csv")
    parser.add_argument("--output", default="data/controlled/controlled_qa_prompt_variants.csv")
    args = parser.parse_args()

    df = pd.read_csv(args.input)

    question_col = "original_question" if "original_question" in df.columns else "question"

    base = (
        df.sort_values(["fact_id", "variant_id"] if "variant_id" in df.columns else ["fact_id"])
        .drop_duplicates("fact_id")
        .copy()
    )

    variant_fns = [
        ("original", clean_question),
        ("leading_space", leading_space),
        ("trailing_space", trailing_space),
        ("space_before_qmark", space_before_question_mark),
        ("no_qmark", no_question_mark),
        ("lower_first_char", lower_first_char),
        ("double_first_space", double_first_space),
    ]

    rows = []

    for _, r in base.iterrows():
        original_q = clean_question(r[question_col])
        seen = set()

        for variant_id, fn in variant_fns:
            controlled_q = fn(original_q)
            final_prompt = qa_template(controlled_q)

            if final_prompt in seen:
                continue

            seen.add(final_prompt)

            rows.append({
                "fact_id": r["fact_id"],
                "variant_id": variant_id,
                "question": final_prompt,
                "original_question": original_q,
                "controlled_question": controlled_q,
                "correct_answer": r["correct_answer"],
                "possible_answers": r.get("possible_answers", ""),
                "type": r.get("type", ""),
            })

    out = pd.DataFrame(rows)
    out.to_csv(args.output, index=False)

    print("Saved:", args.output)
    print("Facts:", out["fact_id"].nunique())
    print("Rows:", len(out))
    print(out.head(10))


if __name__ == "__main__":
    main()
