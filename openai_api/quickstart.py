from openai import OpenAI
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from project root .env
ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY not found in environment. Ensure it exists in the root .env file.")

client = OpenAI(api_key=api_key)

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
