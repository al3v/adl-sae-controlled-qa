import argparse
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input",
        default="reports/controlled_qa_base_v4_strict/activation_pair_type_summary_controlled_qa_base_v4_strict.csv",
        help="CSV file with hidden-state pair-type distances.",
    )

    parser.add_argument(
        "--output",
        default="reports/controlled_qa_base_v4_strict/activation_pair_type_distances_controlled_qa_base_v4_strict.png",
        help="Output plot path.",
    )

    parser.add_argument(
        "--mean-output",
        default="reports/controlled_qa_base_v4_strict/activation_pair_type_mean_summary_controlled_qa_base_v4_strict.csv",
        help="Output CSV with mean distances by layer and pair type.",
    )

    args = parser.parse_args()

    df = pd.read_csv(args.input)

    mean_df = (
        df.groupby(["layer", "pair_type"])[["cosine_distance", "l2_distance"]]
        .mean()
        .reset_index()
    )

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.mean_output).parent.mkdir(parents=True, exist_ok=True)

    mean_df.to_csv(args.mean_output, index=False)

    pair_order = ["correct_correct", "correct_wrong", "wrong_wrong"]
    mean_df["pair_type"] = pd.Categorical(
        mean_df["pair_type"],
        categories=pair_order,
        ordered=True,
    )
    mean_df = mean_df.sort_values(["layer", "pair_type"])

    cosine_pivot = mean_df.pivot(
        index="layer",
        columns="pair_type",
        values="cosine_distance",
    )

    l2_pivot = mean_df.pivot(
        index="layer",
        columns="pair_type",
        values="l2_distance",
    )

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    cosine_pivot.plot(kind="bar", ax=axes[0])
    axes[0].set_title("Hidden-state cosine distance")
    axes[0].set_xlabel("Layer")
    axes[0].set_ylabel("Mean cosine distance")
    axes[0].legend(title="Pair type")

    l2_pivot.plot(kind="bar", ax=axes[1])
    axes[1].set_title("Hidden-state L2 distance")
    axes[1].set_xlabel("Layer")
    axes[1].set_ylabel("Mean L2 distance")
    axes[1].legend(title="Pair type")

    fig.suptitle("Hidden-state distances by pair type")
    fig.tight_layout()

    plt.savefig(args.output, dpi=200)
    print("Saved mean summary:", args.mean_output)
    print("Saved plot:", args.output)


if __name__ == "__main__":
    main()
