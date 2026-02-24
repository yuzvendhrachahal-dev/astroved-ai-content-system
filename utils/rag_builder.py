import json
import faiss
import numpy as np
from urllib.parse import urlparse
from services.openai_service import get_embedding

INPUT_FILE = "data/astroved_links.json"

SERVICE_INDEX = "data/services_index.bin"
SERVICE_META = "data/services_meta.json"

KEYWORDS = ["pooja", "homa", "fire-lab", "instant-pooja"]


def normalize(vec):
    vec = np.array(vec).astype("float32")
    norm = np.linalg.norm(vec)
    if norm == 0:
        return vec
    return vec / norm


def is_service_url(url):
    return any(k in url.lower() for k in KEYWORDS)


def slug_to_title(url):
    slug = urlparse(url).path.strip("/")
    slug = slug.replace("-", " ")
    return slug.title()


def build_service_index():

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    urls = data.get("urls", [])

    service_urls = [u for u in urls if is_service_url(u)]

    print(f"Filtered service URLs: {len(service_urls)}")

    embeddings = []
    metadata = []

    for url in service_urls:

        title = slug_to_title(url) 

        embedding = normalize(get_embedding(title))

        embeddings.append(embedding)

        metadata.append({
            "title": title,
            "url": url
        })

    if not embeddings:
        print("No services found.")
        return

    dim = len(embeddings[0])

    index = faiss.IndexFlatIP(dim)
    index.add(np.array(embeddings).astype("float32"))

    faiss.write_index(index, SERVICE_INDEX)

    with open(SERVICE_META, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print("✅ Services index built successfully.")
    print(f"Indexed services: {len(metadata)}")


if __name__ == "__main__":
    build_service_index()