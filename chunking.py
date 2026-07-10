from langchain_text_splitters import RecursiveCharacterTextSplitter


def get_chunks(text, file_path):
    print("start splitting")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.create_documents([text], metadatas=[{"source": file_path}])
    print("end splitting")
    return chunks
