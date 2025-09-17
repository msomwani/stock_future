
from tools.newsapi_tool import get_news
q="AAPL"
if __name__ == "__main__":
    latest_news=get_news.invoke(q)
    print(latest_news)