from dotenv import load_dotenv
from agents import Agent, ModelSettings, function_tool

load_dotenv()

@function_tool
def get_weather(city: str) -> str:
    """Get the weather for a given city"""
    return f"The weather in {city} is sunny"

agent = Agent(
    name="Haiku Agent",
    instructions="Always respond in haiku format",
    model="gpt-4o-mini",
    tools=[get_weather],
)






