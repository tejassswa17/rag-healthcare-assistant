import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()


class LLMModel:

    def __init__(self):

        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            api_key=os.getenv("GROQ_API_KEY")
        )

    def generate(self, query, context):

        prompt = f"""
You are a professional healthcare assistant.

Use ONLY the provided context to answer the user's question accurately and clearly.

Instructions:
- Understand the user's intent before answering.
- If the user asks a simple question, give a concise answer.
- If the user asks for detailed explanation, provide a well-structured detailed answer.
- Convert retrieved medical text into human-readable explanations.
- Do NOT copy raw chunk text directly.
- Avoid unrelated information.
- Avoid repeating points.
- Use short paragraphs or bullet points when helpful.

For detailed questions, structure the answer using relevant sections such as:
- Definition
- Symptoms
- Causes
- Treatment
- Prevention

Only include sections relevant to the user's question.

If the provided context does not contain enough information, say:
"I don't have enough medical information to answer that clearly."

Context:
{context}

Question:
{query}

Helpful Answer:
"""

        response = self.llm.invoke(prompt)

        return response.content