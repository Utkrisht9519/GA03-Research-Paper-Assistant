import fitz
from mcp import register_tool

@register_tool(
    name="pdf_metadata",
    description="Returns basic metadata from uploaded PDF"
)
def pdf_metadata(input_data):
    file_bytes = input_data.get("pdf_bytes")
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    return {
        "pages": doc.page_count,
        "title": doc.metadata.get("title", "")
    }
