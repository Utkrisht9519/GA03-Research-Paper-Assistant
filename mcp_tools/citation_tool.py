import json
import os
from config import CITATION_DB
from mcp import register_tool

def list_citations(paper_id: str):
    if not os.path.exists(CITATION_DB):
        return []
    with open(CITATION_DB) as f:
        data = json.load(f)
    return data.get(paper_id, [])

@register_tool(
    name="citation_lookup",
    description="Returns citations for a given paper ID"
)
def citation_lookup(input_data):
    paper_id = input_data.get("paper_id")
    return list_citations(paper_id)
