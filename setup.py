from setuptools import setup, find_packages

setup(
    name="paraprompt",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "dask[distributed]",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python library to generate multiple prompt variants using GPT-4 and Dask",
    license="MIT",
    keywords="gpt-4 openai dask prompts",
    url="https://github.com/piollm/para-prompt",
)
