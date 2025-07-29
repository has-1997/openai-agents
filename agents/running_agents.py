import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, SQLiteSession
from agents.tracing import trace

load_dotenv()


async def main():
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant that can answer questions and help with tasks.",
    )
    result = await Runner.run(agent, "Write a haiku about recursion in programming.")
    print(result.final_output)


async def manual_conversation_management():
    agent = Agent(name="Assistant", instructions="Reply very concisely.")
    thread_id = "thread_123"  # Example thread ID
    
    with trace(workflow_name="Conversation", group_id=thread_id):
        # First turn
        result = await Runner.run(agent, "What city is the Golden Gate Bridge in?")
        print(result.final_output)
        # San Francisco

        # Second turn
        new_input = result.to_input_list() + [{"role": "user", "content": "What state is it in?"}]
        result = await Runner.run(agent, new_input)
        print(result.final_output)
        # California

async def automatic_conversation_management():
    agent = Agent(name="Assistant", instructions="Reply very concisely.")

    # Create session instance
    thread_id = "conversation_123"  # Define thread_id
    session = SQLiteSession(thread_id)

    with trace(workflow_name="Conversation", group_id=thread_id):
        # First turn
        result = await Runner.run(
            agent, "What city is the Golden Gate Bridge in?", session=session
        )
        print(result.final_output)
        # San Francisco

        # Second turn - agent automatically remembers previous context
        result = await Runner.run(agent, "What state is it in?", session=session)
        print(result.final_output)
        # California

if __name__ == "__main__":
    asyncio.run(automatic_conversation_management())

