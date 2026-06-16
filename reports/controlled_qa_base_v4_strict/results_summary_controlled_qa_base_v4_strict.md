# Controlled QA Base v4 Strict Results

## Goal

This experiment tests whether small surface/tokenization changes in the prompt can switch Gemma 2B between correct and wrong factual answers.

All prompts use the same fixed QA wrapper:

    Question: ...
    Answer:

Only the question surface form changes, for example:

    Question: Who was the composer of Samson?
    Answer:

    Question:  Who was the composer of Samson?
    Answer:

    Question: Who was the composer of Samson ?
    Answer:

    Question: who was the composer of Samson?
    Answer:

    Question: Who  was the composer of Samson?
    Answer:

## Model and SAE

- Model: google/gemma-2-2b
- SAE: Gemma Scope 2B residual SAE
- Layers analyzed: 6, 9, 12
- Correctness rule: strict grading on the first generated answer segment only
- Accepted answers: correct_answer or dataset-provided possible_answers

## Dataset summary

- Total rows: 420
- Total facts: 60
- Strict correct rows: 168
- Strict wrong rows: 252
- Strict switching facts: 12
- Strict switching rows: 84

## Hidden-state result

Mean hidden-state cosine distances:

| Layer | correct_correct | correct_wrong | wrong_wrong |
|---:|---:|---:|---:|
| 6 | 0.022 | 0.033 | 0.030 |
| 9 | 0.017 | 0.027 | 0.023 |
| 12 | 0.020 | 0.035 | 0.028 |

Across all layers, correct_wrong pairs have larger hidden-state cosine distance than correct_correct pairs.

This means prompt variants that switch factual correctness are farther apart in the model's residual hidden-state space than variants that remain correct.

## SAE result

Mean SAE cosine distances:

| Layer | correct_correct | correct_wrong | wrong_wrong |
|---:|---:|---:|---:|
| 6 | 0.021 | 0.028 | 0.026 |
| 9 | 0.039 | 0.060 | 0.051 |
| 12 | 0.049 | 0.077 | 0.066 |

Across all layers, correct_wrong pairs also have larger SAE cosine distance than correct_correct pairs.

This means prompt variants that switch factual correctness are more separated in sparse SAE feature space than variants that remain correct.

## Interpretation

The result supports the idea that small prompt surface/tokenization changes can affect both the model output and the model's internal representations.

The same fact and expected answer are fixed within each group. Therefore, this is stronger than simply comparing random correct and wrong questions.

The hidden-state analysis shows the effect in the model's residual representations.

The SAE analysis shows the effect in sparse feature space, which is closer to interpretability.

## Careful claim

This experiment supports prompt/tokenization sensitivity, but it does not prove that tokenization alone is the only cause. The prompt surface changes also include small formatting effects such as spacing, capitalization, and punctuation.

A careful final wording is:

> In a fixed QA format, small surface/tokenization changes to the same factual question can switch Gemma 2B between correct and wrong answers, and these switches are visible in both hidden-state space and SAE feature space.

## Important files

- controlled_qa_prompt_variants.csv
- prompt_outputs_controlled_qa_base_v4_strict.csv
- switching_facts_controlled_qa_base_v4_strict.csv
- model_answer_audit_controlled_qa_base_v4_strict.md
- activation_pair_type_summary_controlled_qa_base_v4_strict.csv
- activation_pair_type_mean_summary_controlled_qa_base_v4_strict.csv
- activation_pair_type_distances_controlled_qa_base_v4_strict.png
- sae_pair_type_summary_controlled_qa_base_v4_strict.csv
- sae_pair_type_distances_controlled_qa_base_v4_strict.png
