class AgentState:
    def __init__(self, task: str):
        self.task = task
        self.graph = None
        self.node_outputs = {}
        self.confidence = 0.0
        self.iteration = 0
