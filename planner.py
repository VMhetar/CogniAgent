# planner.py
async def plan(state, llm):
    prompt = f"Break this task into steps as a JSON graph: {state.task}"
    graph = await llm.generate(prompt)
    state.graph = graph