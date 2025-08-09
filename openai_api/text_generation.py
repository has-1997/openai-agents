from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
model = "gpt-5-nano-2025-08-07"

# Generate text from a simple prompt
response = client.responses.create(
    model=model, input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)
