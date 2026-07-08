from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from chunking import chunking

def get_vectorstore(pdf_location):
    chunks = chunking(pdf_location)
    print("start embeddings")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        cache_folder="./models"
    )
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings
    )
    print("end embeddings")
    return vectorstore

books_vectorstore = get_vectorstore("algorithms_book.pdf")
print(books_vectorstore.get(limit=3))