import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urlparse
import time

INPUT_FILE = "data/astroved_links.json"
OUTPUT_FILE = "data/astroved_pages.json"


def extract_slug(url):
    return urlparse(url).path.strip("/")


def scrape_page(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string.strip() if soup.title else ""

        paragraphs = soup.find_all("p")
        content = " ".join([p.get_text().strip() for p in paragraphs])

        return {
            "title": title,
            "url": url,
            "slug": extract_slug(url),
            "content": content[:2000]  
        }

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None


def scrape_all():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    urls = data.get("urls", [])

    results = []

    for i, url in enumerate(urls):
        print(f"[{i+1}/{len(urls)}] Scraping: {url}")
        page_data = scrape_page(url)

        if page_data and page_data["title"]:
            results.append(page_data)

        time.sleep(0.5)  # prevent blocking

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print("✅ Scraping completed.")


if __name__ == "__main__":
    scrape_all()