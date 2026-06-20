"""
TASK 1 (continued) - Pulling real text data for sentiment analysis
Source: Google News RSS (public, no API key needed)

Run this locally (it needs internet access this sandbox doesn't have).
"""

import feedparser  # pip install feedparser
import pandas as pd
from datetime import datetime

QUERIES = [
    "women in STEM",
    "girls education",
    "gender gap higher education",
    "women scientists",
]

def fetch_query(query, max_items=50):
    url = f"https://news.google.com/rss/search?q={query.replace(' ', '+')}&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(url)
    rows = []
    for entry in feed.entries[:max_items]:
        rows.append({
            "text": entry.title,
            "source": entry.get("source", {}).get("title", "unknown"),
            "date": entry.get("published", ""),
            "link": entry.link,
            "query": query,
        })
    return rows

def main():
    all_rows = []
    for q in QUERIES:
        print(f"Fetching: {q}")
        all_rows.extend(fetch_query(q))
    df = pd.DataFrame(all_rows)
    df.to_csv("women_education_news_real.csv", index=False)
    print(f"Saved {len(df)} headlines.")

if __name__ == "__main__":
    main()
