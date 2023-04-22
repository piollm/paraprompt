## Project Name: ParaPrompt

ParaPrompt is a Python library designed to effectively generate imaginative and varied prompts using the GPT-4 API. Its primary goal is to optimize parallelism during the generation process. By utilizing Dask for task distribution, ParaPrompt allows developers to tap into the potential of multiple cores and workers, significantly reducing prompt generation time and enhancing overall application performance.

Developers will find ParaPrompt beneficial when they need multiple prompt variations based on specific criteria and want to maximize resource usage while minimizing generation time. ParaPrompt offers a user-friendly interface for adjusting parallelism levels and generating prompts using the GPT-4 API.

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

Install ParaPrompt using the following command:

```sh
pip install paraprompt
``` 

Usage
Here's a simple example of how to use the ParaPrompt class, focusing on the parallelism capabilities:

python
Copy code
from paraprompt import ParaPrompt

api_key = "your_api_key_here"
input_prompt = "Write a story about a cat and a dog."
variants_criteria = "The prompts should be suitable for short stories, and should include elements of adventure and friendship."

# Set the desired parallelism level
parallelism_level = 5

para_prompt = ParaPrompt(input_prompt).key(api_key).par(parallelism_level).variants(variants_criteria)
generated_prompts = para_prompt.generate()

print(generated_prompts)
By setting the parallelism level, developers can control the degree of task distribution across available workers, tailoring the performance of the prompt generation process to their specific needs and hardware capabilities.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
