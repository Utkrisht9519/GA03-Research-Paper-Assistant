import streamlit as st
from backend.pdf_parser import extract_text
from backend.citation_extractor import extract_references, save_citations
from backend.vector_store import VectorStore
from backend.rag_engine import answer_query

st.set_page_config(page_title="Research Paper Assistant", layout="wide")
st.title("📚 Research Paper Assistant with MCP Tools")

pdf = st.file_uploader("Upload a research paper (PDF)", type="pdf")

if pdf:
    with st.spinner("Processing paper..."):
        text = extract_text(pdf)

        # Save citations
        references = extract_references(text)
        save_citations(pdf.name, references)

        # Build FAISS index
        vs = VectorStore()
        vs.build(text.split("\n"))

    st.success("Paper indexed and citations extracted!")

    st.subheader("Ask a question")
    query = st.text_input("Type your question about the paper")

    if query:
        with st.spinner("Thinking with MCP tools..."):
            answer = answer_query(query, pdf.name)

        st.markdown("### 🧠 Answer")
        st.write(answer)

        st.markdown("### 📚 Extracted References")
        for ref in references[:8]:
            st.write("•", ref)
