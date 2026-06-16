import argparse
import pandas as pd
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="reports/sae_pair_type_summary_base_v2.csv")
    parser.add_argument("--output", default="reports/sae_pair_type_distances_base_v2.png")
    args = parser.parse_args()

    df = pd.read_csv(args.input)

    summary = (
        df.groupby(["layer", "pair_type"])["sae_cosine_distance"]
        .mean()
        .reset_index()
    )

    pivot = summary.pivot(index="layer", columns="pair_type", values="sae_cosine_distance")

    ax = pivot.plot(kind="bar", figsize=(9, 5))
    ax.set_title("Mean SAE cosine distance by layer and correctness pair type")
    ax.set_xlabel("Layer")
    ax.set_ylabel("Mean SAE cosine distance")
    ax.legend(title="Pair type")
    plt.tight_layout()
    plt.savefig(args.output, dpi=200)

    print("Saved plot:", args.output)


if __name__ == "__main__":
    main()
