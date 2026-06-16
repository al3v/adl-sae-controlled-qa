import argparse
from pathlib import Path
import pandas as pd


def to_bool_series(s):
    if s.dtype == bool:
        return s
    return s.astype(str).str.lower().isin(["true", "1", "yes"])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="outputs/prompt_outputs_controlled_qa_base_v4_strict.csv",
        help="Strictly graded model output CSV."
    )
    parser.add_argument(
        "--output",
        default="outputs/switching_facts_controlled_qa_base_v4_strict.csv",
        help="Output CSV containing only switching facts."
    )
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    df["is_correct"] = to_bool_series(df["is_correct"])

    grouped = df.groupby("fact_id")["is_correct"].agg(["sum", "count"]).reset_index()
    grouped["n_correct"] = grouped["sum"]
    grouped["n_wrong"] = grouped["count"] - grouped["sum"]

    switching_ids = grouped[
        (grouped["n_correct"] > 0) & (grouped["n_wrong"] > 0)
    ]["fact_id"]

    switching = df[df["fact_id"].isin(switching_ids)].copy()

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    switching.to_csv(args.output, index=False)

    print("Saved switching facts:", args.output)
    print()
    print("Total rows:", len(df))
    print("Total facts:", df["fact_id"].nunique())
    print("Switching rows:", len(switching))
    print("Switching facts:", switching["fact_id"].nunique())
    print()
    print("Switching fact summary:")
    print(grouped[grouped["fact_id"].isin(switching_ids)][["fact_id", "n_correct", "n_wrong"]])


if __name__ == "__main__":
    main()
