import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, SQLiteSession

load_dotenv()

# Create agent
agent = Agent(
    name="Assistant",
    instructions="Reply very concisely.",
)

async def main():
    # Create a session instance with a session ID
    session = SQLiteSession("conversation_123")

    # First turn
    result = await Runner.run(
        agent, "What city is the Golden Gate Bridge in?", session=session
    )
    print(result.final_output)  # "San Francisco"

    # Second turn - agent automatically remembers previous context
    result = await Runner.run(agent, "What state is it in?", session=session)
    print(result.final_output)  # "California"

    # # Also works with synchronous runner
    # result = Runner.run_sync(agent, "What's the population?", session=session)
    # print(result.final_output)  # "Approximately 39 million"


# Memory operations
async def memory_operations():
    session = SQLiteSession("user_123", "conversations.db")
    # Get all items in a session
    items = await session.get_items()

    # Add new items to a session
    new_items = [
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi there!"}
    ]

    # Remove and return the most recent item
    last_item = await session.pop_item()
    print(last_item)  # {"role": "assistant", "content": "Hi there!"}

    # Clear all items from a session
    await session.clear_session()


if __name__ == "__main__":
    asyncio.run(memory_operations())
