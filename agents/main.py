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

booking_agent = Agent(
    name="Booking Agent",
    instructions="Book a hotel room for a given date",
    model="gpt-4o-mini",
)

refund_agent = Agent(
    name="Refund Agent",
    instructions="Refund a given amount of money",
    model="gpt-4o-mini",
)

triage_agent = Agent(
    name="Triage Agent",
    instructions=(
        "Help the user with their questions."
        "If they ask about booking, handoff to the booking agent."
        "If they ask about refunds, handoff to the refund agent."
    ),
    model="gpt-4o-mini",
    handoffs=[booking_agent, refund_agent],
)

pirate_agent = Agent(
    name="Pirate Agent",
    instructions="Write like a pirate",
)

robot_agent = Agent(
    name="Robot Agent",
    instructions="Write like a robot",
)