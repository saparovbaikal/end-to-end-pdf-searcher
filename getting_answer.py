from google import genai
from os import getenv
from vector_store import vector_store

def get_answer(question,):
    api_key = getenv("GEMINI_API_KEY")
    k_nearest = 5
    context = vector_store.similarity_search(question, k=k_nearest)
    prompt = f"""You are an AI assistant that answers questions using only the provided context.

You will receive:
1. Context retrieved from a knowledge base.
2. A user's question.

Instructions:
- Answer only based on the provided context.
- Do not use your own knowledge or make assumptions.
- If the answer cannot be found in the context, or the information is insufficient, respond exactly:
  "The provided information is not sufficient to answer this question."
- If the context contains information from multiple sources, combine it into a clear and coherent answer.
- Keep your answer concise but informative.
- Use bullet points or numbered lists when they improve readability.
- If the context contains conflicting information, mention the conflict instead of choosing one answer.
- Focus on directly answering the user's question.

Context:
{context}

Question:
{question}

Answer:"""
    client = genai.Client(
        api_key=api_key
    )
    response = client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=prompt
    )
    return response.text