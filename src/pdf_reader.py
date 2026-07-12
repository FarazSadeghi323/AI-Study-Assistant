from pypdf import PdfReader


def get_pdf_page_count(pdf_path):
    reader = PdfReader(pdf_path)
    return len(reader.pages)