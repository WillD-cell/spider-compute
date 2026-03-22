class SpiderModel:
    """
    Universal compute layer for next-gen AI chips.
    Load any model. Deploy to any chip.
    """

    SUPPORTED_CHIPS = ["brainchip", "simulate"]

    def __init__(self, model_path: str):
        self.model_path = model_path
        self.model = None
        self.chip = None
        print(f"[SPIDER] Model loaded: {model_path}")

    def deploy(self, chip: str):
        chip = chip.lower()
        if chip not in self.SUPPORTED_CHIPS:
            raise ValueError(
                f"[SPIDER] Unsupported chip: '{chip}'. "
                f"Supported: {self.SUPPORTED_CHIPS}"
            )
        self.chip = chip
        print(f"[SPIDER] Deploying to chip: {chip}")

        if chip == "brainchip":
            from .chips.brainchip import BrainChipConnector
            self._connector = BrainChipConnector(self.model_path)
        elif chip == "simulate":
            from .chips.simulate import SimulateConnector
            self._connector = SimulateConnector(self.model_path)

        return self

    def run(self, data):
        if self.chip is None:
            raise RuntimeError("[SPIDER] No chip selected. Call .deploy() first.")
        print(f"[SPIDER] Running inference on {self.chip}...")
        return self._connector.infer(data)
