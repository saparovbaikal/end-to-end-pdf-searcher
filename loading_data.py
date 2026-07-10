from extracting_text import extract_text
from chunking import get_chunks
from vector_store import vector_store


def load_data(file_path):
    print("start loading data")
    text = extract_text(file_path)
    chunks = get_chunks(text, file_path)
    vector_store.add_documents(chunks)
    print("end loading data")