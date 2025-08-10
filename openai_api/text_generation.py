from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
model = "gpt-5-nano-2025-08-07"

# Generate text from a simple prompt
# response = client.responses.create(
#     model=model, input="Write a one-sentence bedtime story about a unicorn."
# )

# print(response.output_text)


# Generate text with instructions
# response = client.responses.create(
#     model=model,
#     reasoning={"effort": "low"},
#     instructions="Talk like a pirate",
#     input="Are semicolons optional in JavaScript?",
# )

# print(response.output_text)


# Generate text with messages using different roles
# developer messages provide the system's rules and business logic, like a function definition.
# user messages provide inputs and configuration to which the developer message instructions are applied, like arguments to a function.

# response = client.responses.create(
#     model=model,
#     reasoning={"effort": "low"},
#     input=[
#         {
#             "role": "developer",
#             "content": "Talk like a pirate"
#         },
#         {
#             "role": "user",
#             "content": "Are semicolons optional in JavaScript?"
#         }
#     ]
# )

# print(response.output_text)
