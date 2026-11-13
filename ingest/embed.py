import numpy as np
from sentence_transformers import SentenceTransformer
from chunk import PDF_DIR,extract_pages,chunk_pages

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

def load_chunks():
    all_chunks = []
    for pdf_path in sorted(PDF_DIR.glob("*.pdf")):
        pages = extract_pages(pdf_path)
        for page in pages:                         # one page at a time
            all_chunks.extend(chunk_pages(page))   # page = one dict
    return all_chunks

def main():
    chunks=load_chunks()
    texts=[chunk["text"] for chunk in chunks]
    model=SentenceTransformer(MODEL_NAME)
    vectors=model.encode(texts,batch_size=32,show_progress_bar=True,normalize_embeddings=True)
    print("vectors shape:",vectors.shape)



    question="What is the operating voltage of the esp32?"
    q_vec=model.encode([question],normalize_embeddings=True)[0]

    scores=vectors @ q_vec
    top=np.argsort(scores)[::-1][:5]
    for i in top:
        c=chunks[i]
        print(f"\n{scores[i]:.3f}  {c['doc']}  page {c['page']}")
        print(c["text"][:200], "...")



if __name__=="__main__":
    main()