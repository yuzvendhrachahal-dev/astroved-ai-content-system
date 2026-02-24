import json

def load_links(path="data/astroved_links.json"):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("urls", [])


def filter_pooja_homa_links(urls):
    filtered = []
    
    for url in urls:
        lower_url = url.lower()

        if any(keyword in lower_url for keyword in [
            "pooja",
            "puja",
            "homa",
            "homam"
        ]):
            filtered.append(url)

    return list(set(filtered))


if __name__ == "__main__":
    urls = load_links()
    filtered_urls = filter_pooja_homa_links(urls)

    print(f"Total filtered pooja/homa URLs: {len(filtered_urls)}")

    with open("data/filtered_pooja_homa_links.json", "w", encoding="utf-8") as f:
        json.dump(filtered_urls, f, indent=2)