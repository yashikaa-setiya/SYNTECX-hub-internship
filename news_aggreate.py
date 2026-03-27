import argparse
import pandas as pd
import requests
import json
API_KEY= "9b504c4e5b484b2a954aaa8ac4d81949"

def fetch(keyword):
    url = f"https://newsapi.org/v2/everything?q={keyword}&apikey={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data["articles"]
    except requests.RequestException as e:
        print(f"Error: {e}")
        return []

def save_to_json(articles):
    with open("articles.json","w") as f:
        json.dump(articles,f,indent=4)

def save_to_csv(articles):
    df = pd.DataFrame(articles)
    df.to_csv("news.csv", index=False)
    print("saved to news.csv!")

parse = argparse.ArgumentParser(description="NEWS AGGREATOR")
parse.add_argument("--keyword" ,type=str, default="latest", help="Help fetching news")
parse.add_argument("--source",type=str, help="filter by source name")
args = parse.parse_args()

article = fetch(args.keyword)

seen = set()
unique_articles = []
for item in article:
    if item["title"] not in seen:
        seen.add(item["title"])
        unique_articles.append(item)
article = unique_articles

save_to_json(article)
save_to_csv(article)

if args.source:
    article = [item for item in article if args.source.lower() in item["source"]["name"].lower()]
for items in article:
    print(items["title"])
    print(items["source"]["name"])
    print(items["publishedAt"])
    print("___")


