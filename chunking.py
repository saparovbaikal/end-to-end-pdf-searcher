from langchain_text_splitters import RecursiveCharacterTextSplitter
from pdf_loader import extract_text_from_pdf

def chunking(pdf_location):
    text = extract_text_from_pdf(pdf_location)
    print("start splitting")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    # chunks = [i.page_content for i in text_splitter.create_documents([text])]
    chunks = text_splitter.create_documents([text])
    print("end splitting")
    return chunks

# chunks = chunking("sample.pdf")
# print(type(chunks), chunks)