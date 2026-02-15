# executor.py
async def execute(state, llm):
    # iterate nodes and generate outputs
    for node in state.graph["nodes"]:
        result = await llm.generate(node["instruction"])
        state.node_outputs[node["id"]] = result