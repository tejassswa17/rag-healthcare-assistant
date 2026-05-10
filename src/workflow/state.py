from typing import TypedDict, List


class GraphState(TypedDict):
    query: str
    context: List[str]
    answer: str
    feedback: str
    chat_history: str
    retry_count: int