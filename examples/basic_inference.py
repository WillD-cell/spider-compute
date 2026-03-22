import spider

# Load your model
model = spider.SpiderModel("my_model.pth")

# Deploy to chip
model.deploy(chip="simulate")

# Run inference
result = model.run(data=[1, 2, 3, 4, 5])

print(result)
