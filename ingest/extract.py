from pathlib import Path
import pymupdf as fitz


# Directory containing the PDF files to process.
PDF_DIR = Path("data/pdfs")


def extract_pages(pdf_path):
    # Open one PDF and collect text from pages that are not empty.
    pages=[]
    with fitz.open(pdf_path) as pdf:
        for page_number,page in enumerate(pdf ,start=1):
            text=page.get_text()
            if text.strip():
                pages.append({"doc":pdf_path.name,"page":page_number,"text":text})
    return pages



def main():
    all_pages=[]
    # Process every PDF in the input directory in filename order.
    for pdf_path in sorted(PDF_DIR.glob("*.pdf")):
        pages=extract_pages(pdf_path)
        print(f"Extracted {len(pages)} pages from {pdf_path.name}")
        all_pages.extend(pages)

    print("total pages extracted:",len(all_pages))
    # Display a short preview of the first extracted page.
    print("\nexample text from first page:\n")
    print(all_pages[0]["text"][:500])

if __name__=="__main__":
    main()