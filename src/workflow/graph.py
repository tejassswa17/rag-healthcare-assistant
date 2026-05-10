from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

from src.workflow.state import GraphState
from src.workflow.nodes import chat_node

# Create graph
builder = StateGraph(GraphState)

# Add node
builder.add_node("chat", chat_node)

# Flow
builder.add_edge(START, "chat")
builder.add_edge("chat", END)

# Checkpointer
checkpointer = MemorySaver()

# Compile app
app = builder.compile(
    checkpointer=checkpointer
)