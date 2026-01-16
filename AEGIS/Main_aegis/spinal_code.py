#!/usr/bin/env python3
"""
spinal_code.py

Module to classify queries as REFLEX or ROUTE and as CREATIVE or LOGIC
using a local Ollama model.  If the model cannot determine a type or
style, the function defaults to ROUTE:LOGIC.
"""

import os
import requests
import classifier

# Configuration with environment variable fallbacks
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/generate")
MODEL = os.environ.get("OLLAMA_MODEL", "smollm:135m")  # adjust as needed

def classify_query(query: str) -> str:
    """
    Sends the query to the Ollama endpoint and returns a combined
    classification string in the form "TYPE:STYLE".
    If the model does not provide a clear type or style, the
    function defaults to "ROUTE:LOGIC".
    """
    payload = {
        "model": MODEL,
        "prompt": f"Classify query: REFLEX/ROUTE, CREATIVE/LOGIC. Query: {query}",
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=10)
        response.raise_for_status()
        text = response.json().get("response", "").upper()

        q_type = "REFLEX" if "REFLEX" in text else "ROUTE"
        style = "CREATIVE" if "CREATIVE" in text else "LOGIC"

        return f"{q_type}:{style}"
    except requests.exceptions.RequestException as e:
        print(f"Error contacting Ollama: {e}")
        return "ROUTE:LOGIC"  # fallback on error

def execute_query(classification: str, query: str):
    """
    Executes a query based on its classification.
    For now, it just prints the classification and query.
    """
    print(f"Executing query '{query}' with classification '{classification}'")
    # Call classifier and return its result
    return classifier.classify_and_route(classification, query)

def main():
    query = input("Enter query: ").strip()
    if not query:
        print("No query provided.")
        return
    classification = classify_query(query)
    print(f"({classification} {{{query}}})")
    classifier.classify_and_route(classification, query)

if __name__ == "__main__":
    main()
