import os
from dotenv import load_dotenv
from langchain.tools import tool
import requests
load_dotenv()

NEWS_API_KEY = os.getenv("NEWSAPI_KEY")
BASE_URL = "https://newsapi.org/v2/everything"
@tool
def get_news(query:str)->list:
    """Fetches latest news articles from NewsAPI for a given query"""
    resp=requests.get(
        BASE_URL,
        params={
            "q": query,
            "apiKey": NEWS_API_KEY,
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": 5,
        },
        timeout=10
    )
    print(resp.status_code)
    return resp.json().get("articles",[])