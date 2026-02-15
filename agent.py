"""
Docstring for agent
This module handles asynchronous calls to OpenRouter via MCP.
"""
# agent.py
from state import AgentState
from planner import plan
from executor import execute
from evaluator import evaluate
from llm_client import LLMClient

async def run_agent(task: str):
    llm = LLMClient()
    state = AgentState(task)

    await plan(state, llm)
    await execute(state, llm)
    evaluate(state)

    if state.confidence < 0.85:
        return {"status": "refused"}

    return {
        "status": "success",
        "output": state.node_outputs
    }
