from setuptools import setup, find_packages

setup(
    name="spider-compute",
    version="0.1.0",
    author="Spider Systems",
    description="Universal compute layer for next-gen AI chips",
    long_description=open("README.md").read(),
    url="https://github.com/WillD-cell/spider-compute",
    packages=find_packages(),
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
