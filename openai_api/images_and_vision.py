from dotenv import load_dotenv
from openai import OpenAI
import base64

load_dotenv()

client = OpenAI()
model = "gpt-5-nano-2025-08-07"

# Generate images with Responses
# response = client.responses.create(
#     model=model,
#     input="Generate an image of gray tabby cat hugging an otter with an orange scarf",
#     tools=[{"type": "image_generation"}],
# )

# # Save the image to a file
# image_data = [
#     output.result
#     for output in response.output
#     if output.type == "image_generation_call"
# ]

# if image_data:
#     image_base64 = image_data[0]
#     with open("cat_and_otter.png", "wb") as f:
#         f.write(base64.b64decode(image_base64))


# Analyze the content of an image - Passing a URL
# response = client.responses.create(
#     model=model,
#     input=[
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "input_text",
#                     "text": "What is in this image?"
#                 },
#                 {
#                     "type": "input_image",
#                     "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
#                 },
#             ]
#         }
#     ],
# )

# print(response.output_text)
