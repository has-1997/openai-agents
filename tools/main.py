from dotenv import load_dotenv
from agents import Agent, Runner, FileSearchTool, WebSearchTool, FunctionTool, RunContextWrapper, function_tool
import asyncio
import json
from typing_extensions import TypedDict, Any
from pydantic import BaseModel
from typing import Any

load_dotenv()


async def main():
    agent = Agent(
        name="Assistant",
        tools=[
            WebSearchTool(),
            FileSearchTool(
                max_num_results=2,
                vector_store_ids=["vs_1234567890"],
            ),
        ]
    )
    result = await Runner.run(
        agent,
        "Which coffee shop should I go to, taking into account my preferences and the weather today in SF?",
    )
    print(result.final_output)


# Function tools
class Location(TypedDict):
    lat: float
    long: float

@function_tool
def fetch_weather(location: Location) -> str:
    """Fetch the weather for a given location.

    Args:
        location: The location to fetch the weather for.
    """
    # In real life, we'd fetch the weather from a weather API
    return "sunny"

@function_tool(name_override="fetch_data")
def read_file(ctx: RunContextWrapper[Any], path: str, directory: str | None = None) -> str:
    """Read the contents of a file.

    Args:
        path: The path to the file to read.
        directory: The directory to read the file from.
    """
    # In real life, we'd read the file from the file system
    return "<file contents>"


def main_function_tools():
    agent = Agent(
        name="Assistant",
        tools=[
            fetch_weather,
            read_file,
        ]
    )

    for tool in agent.tools:
        if isinstance(tool, FunctionTool):
            print(tool.name)
            print(tool.description)
            print(json.dumps(tool.params_json_schema, indent=2))
            print()


# Custom function tools
def do_some_work(data: str) -> str:
    return "done"

class FunctionArgs(BaseModel):
    username: str
    age: int

async def run_custom_function_tools(ctx: RunContextWrapper[Any], args: str) -> str:
    parsed = FunctionArgs.model_validate_json(args)
    return do_some_work(data=f"{parsed.username} is {parsed.age} years old")

tool = FunctionTool(
    name="process_user",
    description="Processes extracted user data",
    params_json_schema=FunctionArgs.model_json_schema(),
    on_invoke_tool=run_custom_function_tools,
)


# Agents as tools

async def agent_as_tool():
    spanish_agent = Agent(
        name="Spanish agent",
        instructions="You translate the user's message to Spanish",
    )

    french_agent = Agent(
        name="French agent",
        instructions="You translate the user's message to French",
    )
    
    orchestrator_agent = Agent(
        name="Orchestrator agent",
        instructions=(
            "You are a translation agent. You use the tools given to you to translate."
            "If asked for multiple translations, you call the relevant tool for each language."
        ),
        tools=[
            spanish_agent.as_tool(
                tool_name="translate_to_spanish",
                tool_description="Translates the user's message to Spanish",
            ),
            french_agent.as_tool(
                tool_name="translate_to_french",
                tool_description="Translates the user's message to French",
            ),
        ]
    )
    
    result = await Runner.run(
        orchestrator_agent,
        "Translate the following message to Spanish and French: 'Hello, how are you?'",
    )
    print(result.final_output)




if __name__ == "__main__":
    asyncio.run(agent_as_tool())
