import PyPDF2
import os
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def chunk_text(text: str) -> list:
    """
    將text切分成多個chunk
    """
    chunk = ""
    text_line = text.split("\n")
    chunks = []

    for line in text_line:
        if (line.isspace() or line == "") and chunk != "":
            chunks.append(chunk)
            chunk = ""
        elif (line.isspace() or line == "") and chunk == "":
            continue
        else:
            chunk += line + '\n'
    chunks.append(chunk)
    return chunks
    

def make_document(dir_name: str) -> list:
    pdf_files = os.listdir(dir_name)

    documents = []

    for pdf_file in pdf_files:
        text = extract_text_from_pdf(dir_name + '/' + pdf_file)
        chunk_list = chunk_text(text)
        documents.extend(chunk_list)
    return documents
