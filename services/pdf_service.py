from pypdf import PdfReader

def extract_text_from_pdf(file):
    reader = PdfReader(file.file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text

def get_pdf_page_count(file):
    file.file.seek(0)

    reader = PdfReader(file.file)

    return len(reader.pages)