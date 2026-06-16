import argparse
from pathlib import Path

import pandas as pd
import torch
import torch.nn.functional as F


def to_bool_value(x):
    if isinstance(x, bool):
        return x
    return str(x).lower() in ["true", "1", "yes"]


def cosine_distance(a, b):
    return 1.0 - F.cosine_similarity(a.unsqueeze(0), b.unsqueeze(0)).item()


def l2_distance(a, b):
    return torch.norm(a - b).item()


def active_jaccard_distance(a, b):
    a_active = a > 0
    b_active = b > 0

    intersection = (a_active & b_active).sum().item()
    union = (a_active | b_active).sum().item()

    if union == 0:
        return 0.0

    return 1.0 - (intersection / union)


def get_pair_type(a_correct, b_correct):
    if a_correct and b_correct:
        return "correct_correct"
    if (not a_correct) and (not b_correct):
        return "wrong_wrong"
    return "correct_wrong"


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input",
        default="outputs/sae_features_switching_controlled_qa_base_v4_strict.pt",
        help="SAE feature activation .pt file from the final strict setup.",
    )

    parser.add_argument(
        "--output",
        default="reports/controlled_qa_base_v4_strict/sae_pair_type_summary_controlled_qa_base_v4_strict.csv",
        help="CSV output with pair-type SAE feature distances.",
    )

    args = parser.parse_args()

    rows = torch.load(args.input)

    records = []

    for r in rows:
        records.append(
            {
                "fact_id": r["fact_id"],
                "variant_id": r["variant_id"],
                "layer": int(r["layer"]),
                "is_correct": to_bool_value(r["is_correct"]),
                "feature_acts": r["feature_acts"],
            }
        )

    df = pd.DataFrame(records)

    out_rows = []

    for (fact_id, layer), group in df.groupby(["fact_id", "layer"]):
        group = group.reset_index(drop=True)

        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                a = group.iloc[i]
                b = group.iloc[j]

                pair_type = get_pair_type(a["is_correct"], b["is_correct"])

                out_rows.append(
                    {
                        "fact_id": fact_id,
                        "layer": layer,
                        "variant_a": a["variant_id"],
                        "variant_b": b["variant_id"],
                        "is_correct_a": a["is_correct"],
                        "is_correct_b": b["is_correct"],
                        "pair_type": pair_type,
                        "sae_cosine_distance": cosine_distance(a["feature_acts"], b["feature_acts"]),
                        "sae_l2_distance": l2_distance(a["feature_acts"], b["feature_acts"]),
                        "active_jaccard_distance": active_jaccard_distance(a["feature_acts"], b["feature_acts"]),
                    }
                )

    out = pd.DataFrame(out_rows)

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.output, index=False)

    print("Saved:", args.output)
    print("Pairs:", len(out))
    print()
    print("Mean SAE distances by layer and pair type:")
    print(
        out.groupby(["layer", "pair_type"])[
            ["sae_cosine_distance", "sae_l2_distance", "active_jaccard_distance"]
        ]
        .mean()
        .reset_index()
    )


if __name__ == "__main__":
    main()
