import json
import faiss
import numpy as np
import requests
from urllib.parse import urlparse
from services.openai_service import get_embedding

INPUT_FILE = "data/astroved_links.json"
INDEX_PATH = "data/faiss_index.bin"
META_PATH = "data/metadata.json"


RELEVANT_KEYWORDS = [
    "pooja",
    "homa",
    "festival",
    "special",
    "transit",
    "remedy",
    "temple",
    "yantra",
    "ritual"
]


def is_relevant(url):
    lower = url.lower()
    return any(k in lower for k in RELEVANT_KEYWORDS)


def is_url_working(url):
    try:
        r = requests.head(url, timeout=5, allow_redirects=True)
        return r.status_code == 200
    except:
        return False


def extract_slug(url):
    return urlparse(url).path.strip("/")


def slug_to_title(slug):
    return slug.replace("-", " ").replace(".aspx", "").title()


def build_index():

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    urls = data.get("urls", [])

    embeddings = []
    metadata = []

    for url in urls:

        if not is_relevant(url):
            continue

        if not is_url_working(url):
            continue

        slug = extract_slug(url)
        title = slug_to_title(slug)

        text = f"{title} {slug}"

        embedding = get_embedding(text)

        embeddings.append(embedding)
        metadata.append({
            "title": title,
            "url": url,
            "slug": slug
        })

    if not embeddings:
        print("No relevant URLs found.")
        return

    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype("float32"))

    faiss.write_index(index, INDEX_PATH)

    with open(META_PATH, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print("✅ Filtered FAISS index built.")
    print(f"Indexed: {len(metadata)} pages")


if __name__ == "__main__":
    build_index()