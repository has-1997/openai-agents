import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, SQLiteSession, Session
from typing import List


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
        {"role": "assistant", "content": "Hi there!"},
    ]

    # Remove and return the most recent item
    last_item = await session.pop_item()
    print(last_item)  # {"role": "assistant", "content": "Hi there!"}

    # Clear all items from a session
    await session.clear_session()


# Using pop_item() for corrections
# The pop_item method is particularly useful
# when you want to undo or modify the last item in a conversation
async def corrections():
    agent = Agent(name="Assistant")
    session = SQLiteSession("correction_example")

    result = await Runner.run(agent, "What's 2 + 2?", session=session)
    print(f"Agent: {result.final_output}")

    # User wants to correct their question
    assistant_item = await session.pop_item()  # Remove agent's response
    user_item = await session.pop_item()  # Remove user's question

    # Ask a corrected question
    result = await Runner.run(agent, "What's 2 + 3?", session=session)
    print(f"Agent: {result.final_output}")


# Memory Options


# SQLite memory
async def sqlite_memory():
    # In-memory database (lost when process ends)
    session = SQLiteSession("user_123")

    # Persistent database (saved to file)
    session = SQLiteSession("user_123", "conversations.db")

    agent = Agent(name="Assistant")

    # Use the session
    result = await Runner.run(agent, "What's 2 + 2?", session=session)
    print(f"Agent: {result.final_output}")


# Multiple sessions
async def multiple_sessions():
    session1 = SQLiteSession("session1")
    session2 = SQLiteSession("session2")

    agent = Agent(name="Assistant")

    result1 = await Runner.run(agent, "What's 2 + 2?", session=session1)
    print(f"Agent: {result1.final_output}")

    result2 = await Runner.run(agent, "What's 2 + 3?", session=session2)
    print(f"Agent: {result2.final_output}")


# Custom memory implementations
# You can implement your own session memory by creating a class that follows the Session protocol
class MyCustomSession:
    """Custom session implementation following the Session protocol."""

    def __init__(self, session_id: str):
        self.session_id = session_id
        # Your initialization logic here

    async def get_items(self, limit: int | None = None) -> List[dict]:
        """Retrieve conversation history for this session."""
        # Your implementation here
        pass

    async def add_items(self, items: List[dict]) -> None:
        """Store new items for this session."""
        # Your implementation here
        pass

    async def pop_item(self) -> dict | None:
        """Remove and return the most recent item from the session."""
        # Your implementation here
        pass

    async def clear_session(self) -> None:
        """Clear all items from the session."""
        # Your implementation here
        pass


async def custom_memory():
    agent = Agent(name="Assistant")
    result = await Runner.run(
        agent, "What's 2 + 2?", 
        session=MyCustomSession("my_session")
    )


if __name__ == "__main__":
    asyncio.run(corrections())
