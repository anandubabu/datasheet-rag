import re
from extract import PDF_DIR, extract_pages

# Chunk size and overlap are measured in words.
CHUNK_WORDS=200
OVERLAP_WORDS=40


def clean(text):
    # Collapse repeated whitespace so chunk boundaries are predictable.
    return re.sub(r"\s+", " ", text).strip()


def chunk_pages(page):
    # Split each page into overlapping chunks to preserve context between chunks.
    words=clean(page["text"]).split(" ")
    chunks=[]
    step=CHUNK_WORDS-OVERLAP_WORDS
    for i in range(0, len(words), step):
        piece=words[i:i+CHUNK_WORDS]
        # Ignore very small trailing fragments.
        if len(piece) < 20:
            continue
        chunks.append({"doc":page["doc"], "page":page["page"], "text":" ".join(piece)})
    return chunks


def main():
    all_chunks=[]
    # Extract and chunk every PDF in filename order.
    for pdf_path in sorted(PDF_DIR.glob("*.pdf")):
        for page in extract_pages(pdf_path):
            all_chunks.extend(chunk_pages(page))

    print("total chunks:", len(all_chunks))
    print("\nexample chunk:")
    # Print one sample chunk for a quick manual check.
    print(all_chunks[100])

if __name__ == "__main__":
    main()