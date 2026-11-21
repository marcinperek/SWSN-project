#  Do Embeddings Actually Capture Knowledge Graph Semantics?
This repository contains code related to a project for Semantic Web and Social Networks class.

The aim of the project is to investigate improvements in knowledge graph embeddings since 2021 and evaluate whether these embeddings effectively capture the semantics of knowledge graphs.

## Datasets
- [Yago3-10](https://huggingface.co/datasets/VLyb/YAGO3-10/)
- [FB15k-237](https://huggingface.co/datasets/KGraph/FB15k-237)

## Original paper
The original paper that inspired this project can be found [here](https://link.springer.com/content/pdf/10.1007/978-3-030-77385-4_9.pdf).

## Assessment criteria
https://docs.google.com/document/d/17d47KwN6Nkk38Y1H7e7mwQUJCT2z3WqebeMw6Z-kBdU
## Preprocessing
Processed data is not committed. Generate it with:

```
uv run jupyter nbconvert --to notebook --execute --inplace data/fb15k_preprocessing.ipynb
uv run jupyter nbconvert --to notebook --execute --inplace data/yago_preprocessing.ipynb
```

This writes `data/processed/<dataset>/`: `train/valid/test.tsv` (triple split), `entity_classes.tsv` and `entity_split.tsv` (80/20 entity split per experiment). Terms are defined in `GLOSSARY.md`.
