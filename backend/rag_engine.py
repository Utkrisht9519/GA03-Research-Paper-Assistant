from groq import Groq
from config import LLM_MODEL
from mcp_tools.semantic_search_tool import semantic_search
from mcp_tools.wiki_tool import wiki_lookup
from mcp_tools.citation_tool import citation_lookup


client = Groq()


def run_tools_if_needed(query, paper_id=None):
    """
    Simple agent-style tool router.
    Decides which MCP tool to use based on user intent.
    """

    tools_used = {}

    # 1. Always get semantic context
    context = semantic_search({"query": query})
    tools_used["semantic_search"] = context

    # 2. If user asks for wiki / definition
    if any(x in query.lower() for x in ["what is", "define", "explain", "wiki"]):
        term = query.split()[-1]
        wiki = wiki_lookup({"term": term})
        tools_used["wiki"] = wiki

    # 3. If user asks for references or citations
    if paper_id and any(x in query.lower() for x in ["cite", "reference", "paper", "source"]):
        citations = citation_lookup({"paper_id": paper_id})
        tools_used["citations"] = citations

    return tools_used


def answer_query(query, paper_id=None):
    tools = run_tools_if_needed(query, paper_id)

    context = ""
    if "semantic_search" in tools:
        context += "\n".join(tools["semantic_search"])

    if "wiki" in tools:
        context += "\n\nWikipedia:\n" + str(tools["wiki"])

    if "citations" in tools:
        context += "\n\nCitations:\n" + "\n".join(tools["citations"][:5])

    prompt = f"""
You are a research assistant.

Use the context below to answer the user's question.
Always cite sources when possible.

Context:
{context}

Question:
{query}
"""

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content
