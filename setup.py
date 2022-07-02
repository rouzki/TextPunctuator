# -*- coding: utf-8 -*-

__author__ = "Zakarya ROUZKI"
__email__ = "zakaryarouzki@gmail.com"

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.readlines()
    requirements = [i.strip() for i in requirements]

setup(
    name="TextPunctuator",
    version="1.0.2",
    author="Zakarya ROUZKI",
    author_email="zakaryarouzki@gmail.com",
    description="A package to punctuate text, currently supporting French text, more languages comming soon.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rouzki/text-punctuator",
    packages=find_packages(),
    keywords=['punctuator', 'nlp', 'text', 'transformers', 't5'],
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
)