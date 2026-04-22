import os
import requests
from dotenv import load_dotenv

load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")

def google_serper_search(query: str) -> str:
    """
    Uses Google Serper to fetch recent web information.
    Returns a concise text summary.
    """

    if not SERPER_API_KEY:
        return "Serper API key not configured."

    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "q": query,
        "num": 5
    }

    response = requests.post(url, headers=headers, json=payload, timeout=10)

    if response.status_code != 200:
        return "Failed to fetch external information."

    data = response.json()

    snippets = []
    for item in data.get("organic", []):
        snippet = item.get("snippet")
        if snippet:
            snippets.append(snippet)

    if not snippets:
        return "No relevant external information found."

    return "\n".join(snippets)
