import requests
import json
from dask.distributed import Client, as_completed
import math

class Promptopia:
    def __init__(self, prompt):
        self.prompt = prompt
        self.parallelism = 1
        self.api_key = None
        self.variants_instruction = None
        self.headers = None

    def key(self, api_key):
        self.api_key = api_key
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        return self

    def par(self, parallelism):
        self.parallelism = parallelism
        return self

    def variants(self, variant_instruction):
        self.variants = variant_instruction
        return self

    def generate(self):
        with Client() as client:
            n_workers = len(client.scheduler_info()["workers"])
            n_threads_per_worker = client.nthreads().values()
            total_parallelism = n_workers * sum(n_threads_per_worker) / len(n_threads_per_worker)

            # Calculate the parallelism per worker
            task_par = self._distribute_tasks(self.parallelism, total_parallelism)

            tasks = []
            # Generate a list of delayed tasks
            for i in task_par:
              tasks.append(client.submit(self._generate_prompts, self.prompt, self.variants, i))

            results = []
            for future in as_completed(tasks):
                results.extend(future.result())

            # Return only the number of requested prompts
            return self._merge_results(results[:self.parallelism])

    def _generate_prompts(self, prompt, variants, parallelism):
        data = {
            "model": "gpt-4",
            "messages": [
                {"role": "system", "content": f"Ensure the generated variants are each prompts themselves. Format the response as a json object with keys being 0, 1, etc. and values being one prompt."},
                {"role": "user", "content": f"Please generate {parallelism} number of variants from this prompt: {prompt}; based on this criteria: {variants}."}
            ]
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=self.headers, json=data)

        if response.status_code == 200:
            return json.loads(response.text)['choices']
        else:
            raise Exception(f"Request failed with status code {response.status_code}")

    def _distribute_tasks(self, tasks, slots):
        if tasks <= 0:
            raise ValueError("Number of tasks should be greater than 0")

        slots = int(slots)  # Convert slots to an integer

        base_share = tasks // slots
        remainder = tasks % slots

        shares = [base_share] * slots

        for i in range(remainder):
            shares[i] += 1

        return shares

    def _merge_results(self, results):
        merged = []
        for result in results:
            content = json.loads(result['message']['content'])
            for key in content:
                merged.append(content[key])
        return merged

