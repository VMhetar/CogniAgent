import asyncio
import json

SYSTEM_PROMPT = """
You are an intelligent agent.

Your job is to generate output for the user's request.

Rules:
1. The output must be strict typed code.
2. Edge cases must be handled.
3. Naming must be clear.
4. Return ONLY valid JSON in the format:

{
    "id": 1,
    "reason": "...",
    "output": "..."
}

Do not include markdown.
Do not include explanation outside JSON.
"""


async def generate_output(task: str) -> dict:
    response = await call_openrouter(SYSTEM_PROMPT + "\nTask:\n" + task)

    try:
        parsed = json.loads(response)
        return parsed

    except json.JSONDecodeError:
        return {
            "status": "refused",
            "reason": "Model did not return valid JSON."
        }
