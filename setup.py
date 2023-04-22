from setuptools import setup, find_packages

setup(
    name="paraprompt",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "dask[distributed]",
    ],
    author="piollm",
    description="A Python library to generate multiple prompt variants using GPT-4 and Dask",
    license="MIT",
    keywords="gpt-4 openai parallel prompts",
    url="https://github.com/piollm/paraprompt",
)
