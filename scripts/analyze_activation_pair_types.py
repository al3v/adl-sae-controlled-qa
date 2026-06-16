import argparse
import pandas as pd
import torch
import torch.nn.functional as F


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
    parser.add_argument("--input", default="outputs/hidden_states_switching_v1.pt")
    parser.add_argument("--output", default="reports/activation_pair_type_summary_v1.csv")
    parser.add_argument("--activation-kind", default="last_token_activation")
    args = parser.parse_args()

    rows = torch.load(args.input)

    records = []
    for r in rows:
        records.append({
            "fact_id": r["fact_id"],
            "variant_id": r["variant_id"],
            "layer": r["layer"],
            "is_correct": bool(r["is_correct"]),
            "activation": r[args.activation_kind],
        })

    df = pd.DataFrame(records)
    out_rows = []

    for (fact_id, layer), group in df.groupby(["fact_id", "layer"]):
        group = group.reset_index(drop=True)

        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                a = group.iloc[i]
                b = group.iloc[j]

                pair_type = get_pair_type(a["is_correct"], b["is_correct"])

                out_rows.append({
                    "fact_id": fact_id,
                    "layer": layer,
                    "variant_a": a["variant_id"],
                    "variant_b": b["variant_id"],
                    "is_correct_a": a["is_correct"],
                    "is_correct_b": b["is_correct"],
                    "pair_type": pair_type,
                    "cosine_distance": cosine_distance(a["activation"], b["activation"]),
                    "l2_distance": l2_distance(a["activation"], b["activation"]),
                })

    out = pd.DataFrame(out_rows)
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
