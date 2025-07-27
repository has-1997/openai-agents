from dotenv import load_dotenv
from agents import Agent, ModelSettings, function_tool
from pydantic import BaseModel

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

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

calendar_extractor_agent = Agent(
    name="Calendar Extractor Agent",
    instructions="Extract calendar events from a given text",
    model="gpt-4o-mini",
    output_type=CalendarEvent,
)

calendar_agent = Agent(
    name="Calendar Agent",
    instructions="Create a calendar event based on the user's request",