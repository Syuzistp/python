import requests

def get_articles(api_key, query):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "sortBy": "publishedAt",
        "language": "en",
        "apiKey": api_key
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("articles", [])
    else:
        print(f"Error: Unable to fetch news. Status code {response.status_code}")
        return []

def display_articles(articles, query):
    if not articles:
        print("No articles found for the given category.")
        return

    print(f"News on the topic '{query}'\n")
    for i, article in enumerate(articles[:10], start=1):
        title = article.get("title", "No title")
        source = article.get("source", {}).get("name", "Unknown source")
        published_at = article.get("publishedAt", "Unknown date")
        print(f"{i}. {title}")
        print(f"    {source}")
        print(f"   Published: {published_at}\n")

def main():
    API_KEY = "b4a6ea5892a34846b1076e2fababb0ce"

    query = input("Enter a category (e.g. technology, sports, etc.): ").strip()
    if not query:
        print("Category not found")
        return

    articles = get_articles(API_KEY, query)
    display_articles(articles, query)

if __name__ == "__main__":
    main()

