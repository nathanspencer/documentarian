from docling.document_converter import DocumentConverter
from pathlib import Path

source = "example.pdf"  # document per local path or URL
converter = DocumentConverter()
result = converter.convert(source)
#print(result.document.export_to_markdown())

## Export results
output_dir = Path("scratch")
output_dir.mkdir(parents=True, exist_ok=True)
doc_filename = result.input.file.stem


# Export Markdown format:
with (output_dir / f"{doc_filename}.md").open("w", encoding="utf-8") as fp:
    fp.write(result.document.export_to_markdown())