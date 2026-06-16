import argparse
import ast
import html
import re
import pandas as pd


def normalize_text(x):
    x = "" if pd.isna(x) else str(x)
    x = html.unescape(x)
    x = re.sub(r"<[^>]+>", " ", x)
    x = x.lower()
    x = re.sub(r"[^a-z0-9]+", " ", x)
    x = re.sub(r"\s+", " ", x).strip()
    return x


def parse_possible_answers(x):
    if pd.isna(x):
        return []
    try:
        parsed = ast.literal_eval(str(x))
        if isinstance(parsed, list):
            return [str(a) for a in parsed]
    except Exception:
        pass
    return []


def extract_answer_segment(generated):
    text = "" if pd.isna(generated) else str(generated)

    # In QA format, the model often continues with another generated question.
    # Only grade the first answer segment before the next generated "Question:".
    split_patterns = [
        "\n\nQuestion:",
        "\nQuestion:",
        " Question:",
    ]

    cut = len(text)
    for p in split_patterns:
        idx = text.find(p)
        if idx != -1:
            cut = min(cut, idx)

    return text[:cut].strip()


def is_reasonable_alias(ans):
    norm = normalize_text(ans)

    if not norm:
        return False

    # Avoid very short aliases like "Q", which can match "Question".
    if len(norm) < 3:
        return False

    # Avoid one-character or two-character single-token aliases.
    parts = norm.split()
    if len(parts) == 1 and len(parts[0]) <= 2:
        return False

    return True


def contains_answer(answer_segment, candidate):
    seg = normalize_text(answer_segment)
    cand = normalize_text(candidate)

    if not cand:
        return False

    # Use token-boundary matching after normalization.
    return re.search(rf"(^|\s){re.escape(cand)}($|\s)", seg) is not None


def strict_grade(row):
    answer_segment = extract_answer_segment(row.get("generated_answer", ""))

    candidates = [row.get("correct_answer", "")]
    candidates += parse_possible_answers(row.get("possible_answers", ""))

    candidates = []
    seen = set()

    for a in [row.get("correct_answer", "")] + parse_possible_answers(row.get("possible_answers", "")):
        if not is_reasonable_alias(a):
            continue
        norm = normalize_text(a)
        if norm not in seen:
            seen.add(norm)
            candidates.append(a)

    for cand in candidates:
        if contains_answer(answer_segment, cand):
            return True, cand, answer_segment

    return False, "", answer_segment


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    df = pd.read_csv(args.input)

    strict_results = df.apply(strict_grade, axis=1)

    df["old_is_correct"] = df["is_correct"]
    df["is_correct"] = [x[0] for x in strict_results]
    df["strict_matched_answer"] = [x[1] for x in strict_results]
    df["strict_answer_segment"] = [x[2] for x in strict_results]

    df.to_csv(args.output, index=False)

    print("Saved:", args.output)
    print()
    print("Old correctness counts:")
    print(df["old_is_correct"].value_counts())
    print()
    print("Strict correctness counts:")
    print(df["is_correct"].value_counts())
    print()
    print("Old true but strict false:")
    changed = df[(df["old_is_correct"].astype(bool) == True) & (df["is_correct"] == False)]
    print(len(changed))
    print(changed[["fact_id", "variant_id", "question", "correct_answer", "generated_answer", "strict_answer_segment"]].head(20))


if __name__ == "__main__":
    main()
