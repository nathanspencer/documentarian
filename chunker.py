from docling.document_converter import DocumentConverter
from docling.chunking import HybridChunker

def log_output(chunk_iter):
    with open("log.txt", "a", encoding="utf-8") as f:
        for chunk in chunk_iter:
            f.write(str(chunk) + "\n\n")  # Ensure each chunk is separated

DOC_SOURCE = r"test.pdf"

# When I had set the max to 512, it was still giving me an error saying that the token amount exceeded what the model could handle
max_tokens = 400

doc = DocumentConverter().convert(source=DOC_SOURCE).document

chunker = HybridChunker(max_tokens=max_tokens)
chunk_iter = chunker.chunk(dl_doc=doc)
log_output(chunk_iter)

# for i, chunk in enumerate(chunk_iter):
#     print(f"=== {i} ===")
#     print(f"chunk.text:\n{repr(f'{chunk.text[:300]}…')}")

#     enriched_text = chunker.serialize(chunk=chunk)
#     print(f"chunker.serialize(chunk):\n{repr(f'{enriched_text[:300]}…')}")
#     print()