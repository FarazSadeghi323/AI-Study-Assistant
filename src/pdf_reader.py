# Import the PyMuPDF library.
import fitz


# Return the total number of pages in a PDF file.
def get_pdf_page_count(pdf_path):
    """
    Return the total number of pages in a PDF file.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        int: Total number of pages.
    """

    # Open the PDF file.
    document = fitz.open(pdf_path)

    # Return the total number of pages.
    return document.page_count


# Extract all text from a PDF file.
def extract_text_from_pdf(pdf_path):
    """
    Extract all text from a PDF file.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: All extracted text from the PDF.
    """

    # Open the PDF file.
    document = fitz.open(pdf_path)

    # Store all extracted text.
    text = ""

    # Read every page in the PDF.
    for page in document:

        # Append the current page text.
        text += page.get_text()

    # Return the complete extracted text.
    return text