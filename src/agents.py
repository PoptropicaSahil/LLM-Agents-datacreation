# agents.py

# imports
import os
# import anthropic
from utils import UTILS
from prompts import *


from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


# setup api key
API_KEY = os.getenv("ANTHROPIC_API_KEY")

if not API_KEY:
    API_KEY = input("Enter OpenRouter API key (): ")
# print(f"API key: {API_KEY}")

# anthropic_client = anthropic.Anthropic(api_key=API_KEY)

# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=API_KEY,
)

# Create Analyser Agent
def analyser_agent(sample_data):
    message = client.chat.completions.create(
        model="anthropic/claude-3.5-sonnet",
        max_tokens=400,
        temperature=0.2,
        # n=1,  # only one response, but warning for messages.choices when n=1
        messages=[
            {
                "role": "system", 
                "content": ANALYSER_SYSTEM_PROMPT # noqa: F405
            },
            {
                "role": "user",
                "content": ANALYSER_USER_PROMPT.format(sample_data=sample_data),  # noqa: F405
            },
        ],
    )
    return message.choices[0].message.content

def generator_agent(
    analysis_result,
    sample_data,
    num_rows=30,
):
    message = client.chat.completions.create(
        model="anthropic/claude-3.5-sonnet",
        max_tokens=1500,
        temperature=0.9,
        # n=1,  # only one response, but warning for messages.choices when n=1
        messages=[
            {
                "role": "system", 
                "content": GENERATOR_SYSTEM_PROMPT # noqa: F405
            },
            {
                "role": "user",
                "content": GENERATOR_USER_PROMPT.format(num_rows=num_rows, analysis_result=analysis_result, sample_data=sample_data),  # noqa: F405
            },
        ],
    )
    return message.choices[0].message.content

###########
# Main flow
###########

# Get input from user
file_path = input("Enter file path of the CSV file: ")
file_path = os.path.join('/app/data', file_path)

desired_rows = int(input("Enter number of rows to generate: "))

# Read input data
sample_data = UTILS.read_csv(file_path)
sample_data_str = "\n".join([",".join(row) for row in sample_data]) # csv into a single string

print(f'\nLaunching AI agents to generate {desired_rows} rows of data from {file_path}...')

analysis_result = analyser_agent(sample_data_str)
print(f'>>> Analysis agent result: {analysis_result}')

print(f'{"*"*10} Generating new data... {"*"*10}\n')

# Give the output
output_file = "/app/data/generated_dataset.csv"
headers = sample_data[0]
UTILS.save_to_csv(data=output_file, file_path=output_file, headers=headers)


batch_size = 30
generated_rows = 0

while generated_rows < desired_rows:
    # calculate how many rows to generate in this batch
    rows_to_generate = min(batch_size, desired_rows - generated_rows)

    # generate new rows
    generated_data = generator_agent(analysis_result=analysis_result, sample_data=sample_data_str, num_rows=rows_to_generate)

    # append to output csv
    UTILS.save_to_csv(data=generated_data, 
                      file_path=output_file, 
                    #   headers=headers # if headers enabled for all saves then save_to_csv will only overwrite
                    )

    # update counters
    generated_rows += rows_to_generate

    print(f'>>> Generated {generated_rows}/{desired_rows} rows of data...')

print(f'{"*"*10} Generation complete! {"*"*10}\n')