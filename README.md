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

## Milestone 3

**Selected tools.** We use Python and Jupyter for experiments, uv for reproducible dependencies, and Git and GitHub for collaboration. PyKEEN provides a common training workflow for knowledge graph embeddings. pandas and NumPy support data preparation, NLTK and WordNet supply the type hierarchy, scikit-learn handles entity splits and downstream evaluation, and Matplotlib and SciPy support exploratory analysis.

**Selected models.** Our core comparison uses TransE, RESCAL, ComplEx, DistMult, and ConvE as reference models from Jain et al. (2021). These cover translation, bilinear scoring, and convolution. We add [NodePiece](https://openreview.net/forum?id=xMJWUKJnFSw) to test whether a parameter-efficient, compositional representation can distinguish broad and fine-grained entity types as well as those reference models. We plan to compare entity-type classification on the same prepared splits for FB15k-237 and YAGO3-10.

**Introductory notebook.** [PyKEEN quickstart](data/pykeen_intro.ipynb) trains TransE on the small Nations dataset and retrieves one entity embedding.

**End-to-end MVP.** After running the FB15k-237 preprocessing notebook below, open [FB15k-237 entity typing](data/fb15k_mvp.ipynb). It trains TransE with PyKEEN, aligns embeddings with labels using pandas, and evaluates a simple scikit-learn classifier against a most-frequent-type baseline.

## Preprocessing

Notebooks: [FB15k-237](data/fb15k_preprocessing.ipynb) and [YAGO3-10](data/yago_preprocessing.ipynb).

Processed data is not committed. Generate it with:

```
uv run jupyter nbconvert --to notebook --execute --inplace data/fb15k_preprocessing.ipynb
uv run jupyter nbconvert --to notebook --execute --inplace data/yago_preprocessing.ipynb
```

This writes `data/processed/<dataset>/`: `train/valid/test.tsv` (triple split), `entity_classes.tsv` and `entity_split.tsv` (80/20 entity split per experiment). Terms are defined in `GLOSSARY.md`.
