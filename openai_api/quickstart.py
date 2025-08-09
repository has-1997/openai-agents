from openai import OpenAI
import os
from pathlib import Path
from dotenv import load_dotenv
import asyncio
from agents import Agent, Runner

# Load environment variables from project root .env
ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY not found in environment. Ensure it exists in the root .env file."
    )

client = OpenAI(api_key=api_key)
model = "gpt-5-nano-2025-08-07"

# Generate text from a model
# response = client.responses.create(
#     model="gpt-5",
#     input="Write a one-sentence explanation of the market size for Claims settlement mobile apps that allows users to submit claims and track the status of their claims in the UK only.",
# )

# print(response.output_text)

# Analyze the content of an image
# response = client.responses.create(
#     model="gpt-5",
#     input=[
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "input_text",
#                     "text": "What is in this image?",
#                 },
#                 {
#                     "type": "input_image",
#                     "image_url": "https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/ce/a4/01/cea401e4-97ff-787e-9c02-767137b58dc9/AppIcon-0-0-1x_U007ephone-0-1-0-85-220.png/230x0w.webp",
#                 },
#             ],
#         }
#     ],
# )

# print(response.output_text)

# Use a file URL as input
# response = client.responses.create(
#     model="gpt-5",
#     input=[
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "input_text",
#                     "text": "Analyze the letter and provide a summary of the key points. <50 words",
#                 },
#                 {
#                     "type": "input_file",
#                     "file_url": "https://www.berkshirehathaway.com/letters/2024ltr.pdf",
#                 },
#             ],
#         }
#     ],
# )

# print(response.output_text)


# Upload a file and use it as input
# file = client.files.create(
#     file=open("data/random_data.pdf", "rb"),
#     purpose="user_data",
# )

# print(file.id)

# response = client.responses.create(
#     model="gpt-5",
#     input=[
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "input_file",
#                     "file_id": file.id,
#                 },
#                 {
#                     "type": "input_text",
#                     "text": "Who is the first person in the data?",
#                 },

#             ],
#         }
#     ],
# )

# print(response.output_text)


# Use web search in a response
# response = client.responses.create(
#     model="gpt-5",
#     tools=[{"type": "web_search_preview"}],
#     input="What was a positive news story from today?",
# )

# print(response.output_text)

# Search your files in a response
# response = client.responses.create(
#     model="gpt-4.1",
#     input="What is deep research by OpenAI?",
#     tools=[{
#         "type": "file_search",
#         "vector_store_ids": ["vs_1234567890"],
#     }],
# )

# Call your own function
# tools = [
#     {
#         "type": "function",
#         "name": "get_weather",
#         "description": "Get the temperature for a given location.",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "location": {
#                     "type": "string",
#                     "description": "City and country e.g. London, UK",
#                 }
#             },
#             "required": ["location"],
#             "additionalProperties": False,
#         },
#         "strict": True,
#     }
# ]

# response = client.responses.create(
#     model="gpt-4o",
#     input=[
#         {
#             "role": "user",
#             "content": "What is the weather like in Paris today?",
#         },
#     ],
#     tools=tools,
# )

# print(response.output[0].to_json())


# Call a remote MCP server
# response = client.responses.create(
#     model="gpt-4.1",
#     tools=[
#         {
#             "type": "mcp",
#             "server_label": "deepwiki",
#             "server_url": "https://mcp.deepwiki.com/mcp",
#             "require_approval": "never"
#         }
#     ],
#     input="What transport protocols are supported in the 2025-03-26 version of the MCP spec?",
# )

# print(response.output_text)


# Stream server-sent events from the API
# stream = client.responses.create(
#     model="gpt-4o",
#     input=[
#         {
#             "role": "user",
#             "content": "Say 'double bubble bath' three times fast.",
#         }
#     ],
#     stream=True,
# )

# for event in stream:
#     print(event)


# Build a language triage agent
# spanish_agent = Agent(
#     name="Spanish agent",
#     instructions="You only speak Spanish.",
# )

# english_agent = Agent(
#     name="English agent",
#     instructions="You only speak English.",
# )

# triage_agent = Agent(
#     name="Triage agent",
#     instructions="Handoff to the appropriate agent based on the language of the request.",
#     handoffs=[spanish_agent, english_agent],
# )

# async def language_triage_agent():
#     result = await Runner.run(triage_agent, input="Hola, ¿cómo estás?")
#     print(result.final_output)

# if __name__ == "__main__":
#     asyncio.run(language_triage_agent())
