import os
import re
import json
from config import CITATION_DB

def extract_references(text):
    refs = re.split(r"\n\d+\.\s|\n\[\d+\]\s", text)
    return [r.strip() for r in refs if len(r.strip()) > 30]

def save_citations(paper_id, references):
    # Ensure data directory exists (cloud-safe)
    os.makedirs(os.path.dirname(CITATION_DB), exist_ok=True)

    try:
        with open(CITATION_DB, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    data[paper_id] = references

    with open(CITATION_DB, "w") as f:
        json.dump(data, f, indent=4)

def get_citations(paper_id):
    if not os.path.exists(CITATION_DB):
        return []

    with open(CITATION_DB, "r") as f:
        return json.load(f).get(paper_id, [])
