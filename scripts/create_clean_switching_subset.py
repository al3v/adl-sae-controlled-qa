import argparse
import pandas as pd


BAD_FAILURE_TYPES = {
    "repetition",
    "question_copy",
    "instruction_copy",
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="reports/generation_failure_types_base_v2.csv")
    parser.add_argument("--clean-output", default="outputs/clean_prompt_outputs_base_v2.csv")
    parser.add_argument("--switching-output", default="outputs/clean_switching_facts_base_v2.csv")
    args = parser.parse_args()

    df = pd.read_csv(args.input)

    clean = df[~df["failure_type"].isin(BAD_FAILURE_TYPES)].copy()

    grouped = clean.groupby("fact_id")["is_correct"].agg(["sum", "count"]).reset_index()
    grouped["n_correct"] = grouped["sum"]
    grouped["n_wrong"] = grouped["count"] - grouped["sum"]

    switching_ids = grouped[
        (grouped["n_correct"] > 0) & (grouped["n_wrong"] > 0)
    ]["fact_id"]

    switching = clean[clean["fact_id"].isin(switching_ids)].copy()

    clean.to_csv(args.clean_output, index=False)
    switching.to_csv(args.switching_output, index=False)

    print("Saved clean rows:", args.clean_output)
    print("Saved clean switching rows:", args.switching_output)
    print()
    print("Original rows:", len(df))
    print("Clean rows:", len(clean))
    print("Clean facts:", clean["fact_id"].nunique())
    print("Clean switching facts:", switching["fact_id"].nunique())
    print()
    print("Clean correctness counts:")
    print(clean["is_correct"].value_counts())
    print()
    print("Clean switching fact summary:")
    print(grouped[grouped["fact_id"].isin(switching_ids)][["fact_id", "n_correct", "n_wrong"]])


if __name__ == "__main__":
    main()
