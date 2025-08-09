from dotenv import load_dotenv
from agents import Agent, Runner, FileSearchTool, WebSearchTool
import asyncio

load_dotenv()

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

async def main():
    result = await Runner.run(
        agent,
        "Which coffee shop should I go to, taking into account my preferences and the weather today in SF?",
    )
    print(result.final_output)
    

if __name__ == "__main__":
    asyncio.run(main())