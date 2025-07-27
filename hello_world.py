import os
from dotenv import load_dotenv
from agents import Agent, Runner

load_dotenv('.env.local')  
api_key = os.getenv('OPENAI_API_KEY')

agent = Agent(name="Assistant", instructions="You are a helpful assistant")
result = Runner.run_sync(agent, "Write a haiku about recursion in programming. Less than 10 words.")
print(result.final_output)
