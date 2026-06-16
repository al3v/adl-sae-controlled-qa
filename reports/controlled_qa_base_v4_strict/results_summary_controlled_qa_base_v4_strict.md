# Results summary — controlled_qa_base_v4_strict

## Dataset and generation summary

- Total prompt rows: 420
- Total facts: 60
- Correct rows after strict grading: 167
- Wrong rows after strict grading: 253
- Switching facts: 13
- Switching rows: 91
- Correct switching rows: 48
- Wrong switching rows: 43

## Main interpretation

The key result is that `correct_wrong` pairs generally have larger distances than `correct_correct` pairs across layers 6, 9, and 12. This means variants where answer correctness changes are internally farther apart than variants where both answers stay correct.

This supports a cautious interpretation: small surface/tokenization changes can affect factual answer correctness in Gemma 2B, and those switches are reflected in hidden-state and SAE feature-space distances.

This does not prove that tokenization alone causes hallucination. A safer interpretation is surface/tokenization sensitivity.

## Hidden-state mean distances

|   layer | pair_type       |   cosine_distance |   l2_distance |
|--------:|:----------------|------------------:|--------------:|
|       6 | correct_correct |         0.0233455 |       14.6103 |
|       6 | correct_wrong   |         0.0342415 |       17.8356 |
|       6 | wrong_wrong     |         0.0302556 |       16.4404 |
|       9 | correct_correct |         0.017299  |       19.3779 |
|       9 | correct_wrong   |         0.0281846 |       25.0501 |
|       9 | wrong_wrong     |         0.0232565 |       22.5716 |
|      12 | correct_correct |         0.0199568 |       23.2104 |
|      12 | correct_wrong   |         0.0360528 |       32.1403 |
|      12 | wrong_wrong     |         0.0277248 |       27.6445 |

## SAE feature-space mean distances

|   layer | pair_type       |   sae_cosine_distance |   sae_l2_distance |   active_jaccard_distance |
|--------:|:----------------|----------------------:|------------------:|--------------------------:|
|       6 | correct_correct |             0.0231303 |           9.57778 |                  0.304167 |
|       6 | correct_wrong   |             0.028309  |          10.6431  |                  0.361702 |
|       6 | wrong_wrong     |             0.0258036 |           9.93963 |                  0.342026 |
|       9 | correct_correct |             0.0378957 |          10.5173  |                  0.229228 |
|       9 | correct_wrong   |             0.0617063 |          13.3516  |                  0.286194 |
|       9 | wrong_wrong     |             0.0512711 |          12.1052  |                  0.243983 |
|      12 | correct_correct |             0.0494547 |          15.3774  |                  0.290588 |
|      12 | correct_wrong   |             0.0792397 |          19.9381  |                  0.39867  |
|      12 | wrong_wrong     |             0.0660427 |          17.8102  |                  0.354403 |

## Important output files

- `activation_pair_type_distances_controlled_qa_base_v4_strict.png`
- `activation_pair_type_mean_summary_controlled_qa_base_v4_strict.csv`
- `sae_pair_type_distances_controlled_qa_base_v4_strict.png`
- `sae_pair_type_summary_controlled_qa_base_v4_strict.csv`
- `qa_readable_review_controlled_qa_base_v4_strict.md`
