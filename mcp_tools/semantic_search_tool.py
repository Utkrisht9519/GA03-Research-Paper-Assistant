from backend.vector_store import VectorStore
from mcp import register_tool

@register_tool(
    name="semantic_search",
    description="Runs FAISS search for a given query"
)
def semantic_search(input_data):
    query = input_data.get("query")
    vs = VectorStore()
    vs.load()
    return vs.search(query, k=5)
