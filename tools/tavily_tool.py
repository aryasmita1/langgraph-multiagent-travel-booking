import os
import streamlit as st
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()


def get_secret(key):
    value = os.getenv(key)
    if value:
        return value
    return st.secrets[key]


client = TavilyClient(
    api_key=get_secret("TAVILY_API_KEY")
)


def tavily_search(query):
    response = client.search(
        query=query,
        max_results=5
    )

    results = []

    for i, r in enumerate(response["results"], 1):
        title = r.get("title", "Unknown")
        url = r.get("url", "")
        snippet = r.get("content", "").strip()

        if len(snippet) > 300:
            snippet = snippet[:300].rsplit(" ", 1)[0] + "..."

        results.append(
            f"""{i}. **{title}**
{url}
{snippet}
"""
        )

    return "\n\n".join(results)
