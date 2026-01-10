from groq import Groq

def answer_query(query, context):
    client = Groq()
    prompt = f"""
    Use the context to answer.
    Cite sources where possible.

    Context:
    {context}

    Question:
    {query}
    """

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
