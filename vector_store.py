from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


print("start loading vector store")
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    cache_folder="./models"
)
vector_store = Chroma(
    persist_directory="vector_db",
    embedding_function=embeddings
)
print("end loading vector store")
