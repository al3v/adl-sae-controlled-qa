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
        default="outputs/hidden_states_switching_controlled_qa_base_v4_strict.pt",
        help="Hidden-state activation .pt file from the final strict setup.",
    )

    parser.add_argument(
        "--output",
        default="reports/controlled_qa_base_v4_strict/activation_pair_type_summary_controlled_qa_base_v4_strict.csv",
        help="CSV output with pair-type hidden-state distances.",
    )

    parser.add_argument(
        "--activation-kind",
        default="last_token_activation",
        choices=["last_token_activation", "mean_prompt_activation"],
        help="Which hidden-state representation to compare.",
    )

    args = parser.parse_args()

    rows = torch.load(args.input)

    records = []

    for r in rows:
        records.append(
            {
                "fact_id": r["fact_id"],
                "variant_id": r["variant_id"],
                "layer": r["layer"],
                "is_correct": to_bool_value(r["is_correct"]),
                "activation": r[args.activation_kind],
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
                        "cosine_distance": cosine_distance(a["activation"], b["activation"]),
                        "l2_distance": l2_distance(a["activation"], b["activation"]),
                    }
                )

    out = pd.DataFrame(out_rows)

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.output, index=False)

    print("Saved:", args.output)
    print("Pairs:", len(out))
    print()
    print("Mean distances by layer and pair type:")
    print(
        out.groupby(["layer", "pair_type"])[["cosine_distance", "l2_distance"]]
        .mean()
        .reset_index()
    )


if __name__ == "__main__":
    main()
