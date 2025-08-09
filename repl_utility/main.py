import asyncio
from dotenv import load_dotenv
from agents import Agent, run_demo_loop

load_dotenv()

async def main():
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant.",
    )
    
    await run_demo_loop(agent)
    
if __name__ == "__main__":
    asyncio.run(main())