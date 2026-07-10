from google import genai

from os import getenv

from extracting_text import extract_text
from chunking import get_chunks
from getting_vector_store import get_vector_store


# import hashlib
#
#
# def get_file_hash(file_path):
#     sha256 = hashlib.sha256()
#     with open(file_path, "rb") as f:
#         while chunk := f.read(8192):
#             sha256.update(chunk)
#     return sha256.hexdigest()


def load_pdf(file_path):
    text = extract_text(file_path)
    chunks = get_chunks(text, file_path)
    vector_store.add_documents(chunks)


def get_answer(question):
    api_key = getenv("GEMINI_API_KEY")
    k_nearest = 5
    context = vector_store.similarity_search(question, k=k_nearest)
    prompt = f"""Ты — помощник, который отвечает на вопросы только на основе предоставленного контекста.

Тебе будут переданы:
1. Контекст, найденный в базе знаний.
2. Вопрос пользователя.

Правила:
- Отвечай только на основе контекста.
- Если ответа в контексте нет или информации недостаточно, честно скажи: "В предоставленных данных нет достаточной информации, чтобы ответить на этот вопрос."
- Не придумывай факты и не используй свои знания, если они отсутствуют в контексте.
- Если контекст содержит несколько частей информации, объедини их в один понятный ответ.
- Отвечай кратко, но достаточно подробно.
- Если возможно, используй списки для лучшей читаемости.

Контекст:
{context}

Вопрос:
{question}

Ответ:"""
    client = genai.Client(
        api_key=api_key
    )
    response = client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=prompt
    )
    return response.text


vector_store = get_vector_store()
# load_pdf("algorithms_book.pdf")
answer = get_answer("what is a sample algorithmic problem")
print(answer)


