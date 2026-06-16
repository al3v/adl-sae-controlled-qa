import argparse
import itertools
import pandas as pd
import torch
import torch.nn.functional as F


def cosine_distance(a, b):
    return 1.0 - F.cosine_similarity(a.unsqueeze(0), b.unsqueeze(0)).item()


def l2_distance(a, b):
    return torch.norm(a - b).item()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="outputs/hidden_states_switching_v1.pt")
    parser.add_argument("--output", default="reports/activation_distance_summary_v1.csv")
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
        correct_rows = group[group["is_correct"] == True]
        wrong_rows = group[group["is_correct"] == False]

        if len(correct_rows) == 0 or len(wrong_rows) == 0:
            continue

        for _, c in correct_rows.iterrows():
            for _, w in wrong_rows.iterrows():
                out_rows.append({
                    "fact_id": fact_id,
                    "layer": layer,
                    "correct_variant": c["variant_id"],
                    "wrong_variant": w["variant_id"],
                    "cosine_distance": cosine_distance(c["activation"], w["activation"]),
                    "l2_distance": l2_distance(c["activation"], w["activation"]),
                })

    out = pd.DataFrame(out_rows)
    out.to_csv(args.output, index=False)

    print("Saved:", args.output)
    print("Pairs:", len(out))
    print()
    print("Mean distances by layer:")
    print(out.groupby("layer")[["cosine_distance", "l2_distance"]].mean())


if __name__ == "__main__":
    main()
