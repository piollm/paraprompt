## Project Name: ParaPrompt

ParaPrompt is a Python library designed to efficiently generate creative and diverse prompts using the GPT-4 API. The primary focus of this library is to maximize the parallelism capabilities during the generation process. By leveraging Dask for task distribution, ParaPrompt enables developers to harness the power of multiple cores and workers, significantly reducing the time spent on generating prompts and improving overall application performance.

Developers would want to use ParaPrompt in situations where they require multiple prompt variations based on specific criteria, and where they need to optimize resource usage and minimize generation time. ParaPrompt provides an easy-to-use interface for customizing parallelism and generating prompts using the GPT-4 API.

## Features

- Efficient parallel prompt generation utilizing Dask
- Set API key for GPT-4 API authentication
- Customize parallelism level for task distribution across available workers
- Provide criteria for generating diverse prompt variants
- Retrieve generated prompts using the GPT-4 API

## Requirements

- Python 3.6 or higher
- Dask
- requests

## Installation

Install the required dependencies using the following command:

\`\`\`sh
pip install dask distributed requests
\`\`\`

Clone the repository and include the \`promptopia.py\` file in your project.

## Usage

Here's a simple example of how to use the ParaPrompt class, focusing on the parallelism capabilities:

\`\`\`python
from promptopia import ParaPrompt

api_key = "your_api_key_here"
input_prompt = "Write a story about a cat and a dog."
variants_criteria = "The prompts should be suitable for short stories, and should include elements of adventure and friendship."

# Set the desired parallelism level
parallelism_level = 5

para_prompt = ParaPrompt(input_prompt).key(api_key).par(parallelism_level).variants(variants_criteria)
generated_prompts = para_prompt.generate()

print(generated_prompts)
\`\`\`

By setting the parallelism level, developers can control the degree of task distribution across available workers, tailoring the performance of the prompt generation process to their specific needs and hardware capabilities.
