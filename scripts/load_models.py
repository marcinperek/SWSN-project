from pykeen.models import model_resolver


MODEL_NAMES = (
    # original paper baselines
    "TransE",
    "RESCAL",
    "ComplEx",
    "DistMult",
    "ConvE",
    # project comparison models
    "RotatE",
    "TuckER",
    "BoxE",
    "RGCN",
    "MuRE",
    "QuatE",
    "CompGCN",
    "CP",
    "PairRE",
    "NodePiece",
)


def main() -> None:
    for name in MODEL_NAMES:
        model_class = model_resolver.lookup(name)
        print(f"Loaded {name}: {model_class.__module__}.{model_class.__name__}")


if __name__ == "__main__":
    main()
