import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner

load_dotenv()


async def main():
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant that can answer questions and help with tasks.",
    )
    result = await Runner.run(agent, "Write a haiku about recursion in programming.")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())