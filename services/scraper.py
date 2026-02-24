import cloudscraper
from bs4 import BeautifulSoup

class ContentScraper:

    def scrape(self, url: str):

        scraper = cloudscraper.create_scraper()

        response = scraper.get(url, timeout=20)

        if response.status_code != 200:
            raise Exception(f"HTTP Error: {response.status_code}")

        soup = BeautifulSoup(response.text, "lxml")

        title = soup.title.text.strip() if soup.title else ""

        meta_tag = soup.find("meta", {"name": "description"})
        meta = meta_tag["content"].strip() if meta_tag else ""

        paragraphs = [
            p.text.strip()
            for p in soup.find_all("p")
            if len(p.text.strip()) > 50
        ]

        content = " ".join(paragraphs)

        return {
            "title": title,
            "meta": meta,
            "content": content,
            "word_count": len(content.split())
        }
