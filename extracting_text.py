import pdfplumber
import re


def clean_text(text):
    text = re.sub(r"-\n", "", text)
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_text(pdf_location):
    print("start loading")
    with pdfplumber.open(pdf_location) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
        print("end loading")
        return clean_text(text)