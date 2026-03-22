# Spider Compute

**Universal compute layer for next-gen AI chips.**

Spider Compute lets you take any AI model and run it on neuromorphic, photonic, 
and reversible computing hardware — without rewriting anything.
```python
import spider

model = spider.SpiderModel("my_model.pth")
model.deploy(chip="brainchip")
result = model.run(data)
```

## Supported Chips

| Chip | Type | Status |
|------|------|--------|
| BrainChip Akida | Neuromorphic | In development |
| Simulate | Software simulation | ✅ Ready |
| Vaire | Reversible | Coming soon |
| Lightmatter | Photonic | Coming soon |

## Install
```bash
pip install spider-compute
```

## Why Spider

Every next-gen chip has its own SDK. Its own rules. Its own hell.
Spider sits in the middle. One API. Every chip.

---

Built by [Spider Systems](https://github.com/WillD-cell)
