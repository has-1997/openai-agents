import os
from dotenv import load_dotenv
from agents import Agent


load_dotenv(".env.local")
api_key = os.getenv("OPENAI_API_KEY")

agent = Agent(
    name="Math Tutor",
    instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
)
