from services.rag_engine import get_best_service

VEDIC_TERMS = [
    "Shani", "Saturn",
    "Rahu", "Ketu",
    "Navagraha",
    "Lakshmi",
    "Ganesha",
    "Shiva",
    "Vishnu",
    "Krishna",
    "Dosha",
    "Nakshatra",
    "Transit",
    "Janmashtami",
    "Diwali"
]


def auto_link_content(content):

    used_urls = set()

    for term in VEDIC_TERMS:

        if term not in content:
            continue

        result = get_best_service(term)

        if not result:
            continue

        url = result["url"]

        if url in used_urls:
            continue

        content = content.replace(
            term,
            f"[{term}]({url})",
            1
        )

        used_urls.add(url)

    return content