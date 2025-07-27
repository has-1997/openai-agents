import os
from dotenv import load_dotenv
from agents import Agent, Runner, GuardrailFunctionOutput, InputGuardrail
from agents.exceptions import InputGuardrailTripwireTriggered

import asyncio
from pydantic import BaseModel

load_dotenv(".env.local")
api_key = os.getenv("OPENAI_API_KEY")


class HomeworkOutput(BaseModel):
    is_homework: bool
    reasoning: str


guardrail_agent = Agent(
    name="Guardrail Agent",
    instructions="Check if the user's question is a homework question",
    output_type=HomeworkOutput,
)

history_tutor_agent = Agent(
    name="History Tutor",
    handoff_description="Specialist agent for historical questions",
    instructions="You provide assistance with historical queries. Explain important events and context clearly.",
)

math_tutor_agent = Agent(
    name="Math Tutor",
    handoff_description="Specialist agent for math questions",
    instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
)


async def homework_guardrail(ctx, agent, input_data):
    result = await Runner.run(guardrail_agent, input_data, context=ctx.context)
    final_output = result.final_output_as(HomeworkOutput)
    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=not final_output.is_homework,
    )


triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which agent to hand off to based on the user's question",
    handoffs=[history_tutor_agent, math_tutor_agent],
    input_guardrails=[
        InputGuardrail(guardrail_function=homework_guardrail),
    ],
)


async def main():
    try:
        result = await Runner.run(triage_agent, "What is the capital of France?")
        print(result.final_output)
    except InputGuardrailTripwireTriggered as e:
        print("Guardrail blocked this input:", e)
    
    try:
        result = await Runner.run(triage_agent, "What is the meaning of life?")
        print(result.final_output)
    except InputGuardrailTripwireTriggered as e:
        print("Guardrail blocked this input:", e)


if __name__ == "__main__":
    asyncio.run(main())
