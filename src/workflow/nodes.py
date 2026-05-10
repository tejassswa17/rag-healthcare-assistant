from src.retrieval.retriever import Retriever
from src.workflow.state import GraphState
from src.llm.llm import LLMModel

retriever = Retriever()
llm = LLMModel()


def chat_node(state: GraphState) -> GraphState:

    query = state.get("query", "")
    feedback = state.get("feedback", "")
    chat_history = state.get("chat_history", "")
    retry_count = state.get("retry_count", 0)

    # -----------------------------
    # QUERY REWRITING STEP
    # -----------------------------

    rewrite_prompt = f"""
You are a query rewriting assistant.

Conversation History:
{chat_history}

Current User Question:
{query}

Rewrite the current question into a clear standalone healthcare query.

Rules:
- Resolve references like it, its, they, them.
- Keep the meaning unchanged.
- Return ONLY the rewritten query.
"""

    rewritten_query = llm.llm.invoke(rewrite_prompt).content.strip()

    # -----------------------------
    # RETRIEVAL
    # -----------------------------

    results = retriever.search(rewritten_query)

    # No relevant medical information
    if not results or len(results) == 0:

        state["answer"] = (
            "I don't have enough medical information "
            "in the knowledge base to answer that clearly."
        )

        return state

    # Convert chunks into text
    context = "\n".join(results)

    # -----------------------------
    # FIRST GENERATION
    # -----------------------------

    if feedback == "":

        answer = llm.generate(rewritten_query, context)

    # -----------------------------
    # REFINEMENT GENERATION
    # -----------------------------

    else:

        refine_prompt = f"""
You are a professional healthcare assistant.

The user was not satisfied with the previous answer.

Conversation History:
{chat_history}

Current Question:
{query}

Rewritten Question:
{rewritten_query}

User Feedback:
{feedback}

Instructions:
- Improve and refine the previous answer
- Make the answer clearer and more informative
- Do not repeat the same wording
- Keep the answer concise and structured
- Use ONLY the provided medical context
- Do NOT use outside knowledge
- Do NOT guess information

Improved Answer:
"""

        answer = llm.generate(refine_prompt, context)

    # -----------------------------
    # STORE FULL CONVERSATION HISTORY
    # -----------------------------

    updated_history = f"""
{chat_history}

###
User: {query}
Rewritten Query: {rewritten_query}
Bot: {answer}
"""

    # -----------------------------
    # UPDATE STATE
    # -----------------------------

    state["context"] = results
    state["answer"] = answer
    state["chat_history"] = updated_history
    state["retry_count"] = retry_count + 1

    return state