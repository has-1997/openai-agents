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
        agent, "What's 2 + 2?", session=MyCustomSession("my_session")
    )


# Session management
async def session_management():
    # Clear a session when conversation should start fresh
    session = SQLiteSession("user_123")
    await session.clear_session()

    # Different agents can share the same session
    support_agent = Agent(name="Support")
    billing_agent = Agent(name="Billing")
    session = SQLiteSession("user_123")

    # Both agents can access the same session
    result1 = await Runner.run(
        support_agent, "Help me with my account", session=session
    )
    result2 = await Runner.run(billing_agent, "I need to pay my bill", session=session)
    print(f"Support: {result1.final_output}")
    print(f"Billing: {result2.final_output}")


# Complete example
async def main():
    # Create an agent
    agent = Agent(name="Assistant", instructions="Reply very concisely.")

    # Create a session instance that will persist across runs
    session = SQLiteSession("conversation_123", "conversation_history.db")

    print("=== Sessions Example ===")
    print("The agent will remember previous messages automatically.\n")

    # First turn
    print("First turn:")
    print("User: What city is the Golden Gate Bridge in?")
    result = await Runner.run(agent, "What city is the Golden Gate Bridge in?", session=session)
    print(f"Agent: {result.final_output}")
    print()

    # Second turn - the agent will remember the previous conversation
    print("Second turn:")
    print("User: What state is it in?")
    result = await Runner.run(agent, "What state is it in?", session=session)
    print(f"Agent: {result.final_output}")
    print()

    # Third turn - the agent will remember the previous conversation
    print("Third turn:")
    print("User: What's the population of the city?")
    result = await Runner.run(agent, "What's the population of that state?", session=session)
    print(f"Agent: {result.final_output}")
    print()

    print("=== Conversation Complete ===")
    print("Notice how the agent remembered the context from previous turns!")
    print("Sessions automatically handles conversation history.")

if __name__ == "__main__":
    asyncio.run(main())
