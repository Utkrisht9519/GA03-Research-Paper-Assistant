import requests
from config import WIKI_API
from mcp import register_tool

@register_tool(
    name="wiki_lookup",
    description="Returns a summary from Wikipedia"
)
def wiki_lookup(input_data):
    term = input_data.get("term", "")
    url = WIKI_API + term
    r = requests.get(url)
    if r.status_code != 200:
        return {"error": "No summary found"}
    return r.json().get("extract", "")
