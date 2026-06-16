# ADL SAE Controlled QA Experiment

This repository contains the final controlled experiment for my Applied Deep Learning project on LLM factual QA sensitivity.

## Project goal

The goal is to study whether small surface/tokenization changes to the same factual question can switch a language model between correct and wrong answers, and whether these switches are visible in internal representations.

The experiment uses Gemma 2B and analyzes both hidden states and Sparse Autoencoder features.

## Main idea

For each factual question, I created small prompt variants while keeping the meaning almost unchanged.

Example variants:

- original question
- leading space
- trailing space
- space before question mark
- no question mark
- lowercased first character
- double first space

The model was prompted using a fixed QA format:

    Question: ...
    Answer:

The generated answers were strictly graded using only the first answer segment.

## Main result

In the final strict controlled QA setup:

- 60 facts were tested
- 420 prompt rows were generated
- 12 facts showed switching behavior
- Switching means that some variants of the same fact were answered correctly, while other variants were answered wrongly

For the switching facts, I compared internal representations between prompt variants.

The key pattern was:

    correct_wrong distance > correct_correct distance

This appeared in both:

- hidden-state space
- SAE feature space

across layers 6, 9, and 12.

## Careful conclusion

The results provide evidence that small surface/tokenization changes can affect factual answer correctness in Gemma 2B. These correctness switches are associated with larger internal representation differences in both hidden-state and SAE feature space.

This does not prove that tokenization alone causes hallucination. A safer interpretation is surface/tokenization sensitivity.

## Important files

- `data/controlled/controlled_qa_prompt_variants.csv`  
  Final controlled prompt variant dataset.

- `reports/controlled_qa_base_v4_strict/results_summary_controlled_qa_base_v4_strict.md`  
  Main result summary.

- `reports/controlled_qa_base_v4_strict/qa_readable_review_controlled_qa_base_v4_strict.md`  
  Human-readable review of switching facts, expected answers, model answers, and correctness labels.

- `reports/controlled_qa_base_v4_strict/activation_pair_type_mean_summary_controlled_qa_base_v4_strict.csv`  
  Hidden-state distance summary.

- `reports/controlled_qa_base_v4_strict/activation_pair_type_distances_controlled_qa_base_v4_strict.png`  
  Hidden-state distance plot.

- `reports/controlled_qa_base_v4_strict/sae_pair_type_summary_controlled_qa_base_v4_strict.csv`  
  SAE feature-space distance summary.

- `reports/controlled_qa_base_v4_strict/sae_pair_type_distances_controlled_qa_base_v4_strict.png`  
  SAE feature-space distance plot.

## Project status

This repository contains the cleaned final version of the experiment, prepared for discussion and presentation.
