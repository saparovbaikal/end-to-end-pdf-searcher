import pdfplumber

with pdfplumber.open("sample.pdf") as pdf:
    text = []
    for page in pdf.pages:
        text.append(page.extract_text())
    print(text)
