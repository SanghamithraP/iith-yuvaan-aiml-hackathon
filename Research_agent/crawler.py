import requests
from bs4 import BeautifulSoup

def get_google_news(company):
    
    query = company + " company news"
    url = f"https://news.google.com/search?q={query}"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = []

    for item in soup.find_all("a"):
        text = item.text
        if len(text) > 30:
            headlines.append(text)

    return headlines[:10]


def search_litigation(company):

    query = company + " lawsuit case fraud"
    url = f"https://www.google.com/search?q={query}"

    response = requests.get(url)

    soup = BeautifulSoup(response.text,"html.parser")

    results = []

    for g in soup.find_all('h3'):
        results.append(g.text)

    return results[:5]