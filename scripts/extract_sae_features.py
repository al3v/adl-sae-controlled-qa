import argparse
import pandas as pd
import torch
from sae_lens import SAE


def load_sae_for_layer(layer, device):
    release = "gemma-scope-2b-pt-res-canonical"
    sae_id = f"layer_{layer}/width_16k/canonical"

    loaded = SAE.from_pretrained(
        release=release,
        sae_id=sae_id,
        device=device,
    )

    if isinstance(loaded, tuple):
        sae = loaded[0]
    else:
        sae = loaded

    sae.eval()
    return sae


def encode_with_sae(sae, activation):
    activation = activation.to(next(sae.parameters()).device)

    with torch.no_grad():
        if activation.ndim == 1:
            activation = activation.unsqueeze(0)

        feature_acts = sae.encode(activation)

        if isinstance(feature_acts, tuple):
            feature_acts = feature_acts[0]

    return feature_acts.squeeze(0).detach().cpu().float()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="outputs/hidden_states_switching_base_v2.pt")
    parser.add_argument("--output", default="outputs/sae_features_switching_base_v2.pt")
    parser.add_argument("--summary-output", default="reports/sae_feature_summary_base_v2.csv")
    parser.add_argument("--activation-kind", default="last_token_activation")
    parser.add_argument("--layers", default="6,9,12")
    parser.add_argument("--top-k", type=int, default=20)
    args = parser.parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    layers = [int(x.strip()) for x in args.layers.split(",")]

    print("Device:", device)
    if torch.cuda.is_available():
        print("GPU:", torch.cuda.get_device_name(0))

    rows = torch.load(args.input)
    print("Loaded hidden-state rows:", len(rows))

    sae_by_layer = {}

    feature_rows = []
    summary_rows = []

    for layer in layers:
        print(f"Loading SAE for layer {layer}...")
        sae_by_layer[layer] = load_sae_for_layer(layer, device)

    for i, row in enumerate(rows):
        layer = int(row["layer"])

        if layer not in layers:
            continue

        sae = sae_by_layer[layer]
        activation = row[args.activation_kind]

        feature_acts = encode_with_sae(sae, activation)

        nonzero = feature_acts > 0
        n_active = int(nonzero.sum().item())
        l1_norm = float(feature_acts.abs().sum().item())
        l2_norm = float(torch.norm(feature_acts).item())
        max_value = float(feature_acts.max().item())

        top_values, top_indices = torch.topk(
            feature_acts,
            k=min(args.top_k, feature_acts.numel())
        )

        feature_rows.append({
            "fact_id": row["fact_id"],
            "variant_id": row["variant_id"],
            "layer": layer,
            "is_correct": bool(row["is_correct"]),
            "feature_acts": feature_acts,
        })

        summary_rows.append({
            "fact_id": row["fact_id"],
            "variant_id": row["variant_id"],
            "layer": layer,
            "is_correct": bool(row["is_correct"]),
            "n_active_features": n_active,
            "feature_l1_norm": l1_norm,
            "feature_l2_norm": l2_norm,
            "max_feature_value": max_value,
            "top_feature_indices": " ".join(map(str, top_indices.tolist())),
            "top_feature_values": " ".join(f"{x:.6f}" for x in top_values.tolist()),
        })

        print(f"[{i+1}/{len(rows)}] layer={layer} fact={row['fact_id']} variant={row['variant_id']} active={n_active}")

    torch.save(feature_rows, args.output)
    pd.DataFrame(summary_rows).to_csv(args.summary_output, index=False)

    print()
    print("Saved SAE features:", args.output)
    print("Saved summary:", args.summary_output)
    print("Rows:", len(summary_rows))


if __name__ == "__main__":
    main()
