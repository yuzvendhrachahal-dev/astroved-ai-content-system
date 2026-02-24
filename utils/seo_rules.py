SEO_RULES = {
    # Core Structure
    "title_min": 50,
    "title_max": 60,
    "meta_min": 150,
    "meta_max": 160,

    # Content Depth
    "min_word_count": 1800,
    "optimal_word_count": 2200,

    # Headings
    "min_h2": 6,
    "min_h3": 12,
    "max_h1": 1,

    # FAQ
    "min_faq": 6,

    # Internal Linking
    "min_internal_links": 5,

    # Vedic Terminology
    "mandatory_terms": [
        "Pooja",
        "Homa",
        "Nakshatra",
        "Dosha",
        "Graha",
        "Dasha"
    ],

    # Brand
    "brand_term": "AstroVed",

    # Avoid terms
    "avoid_terms": [
        "western astrology",
        "horoscope app",
        "psychic reading"
    ]
}


def get_rules_summary():
    return f"""
ASTROVED AI SEO PRODUCTION RULES (2026)

• Title: {SEO_RULES['title_min']}–{SEO_RULES['title_max']} chars
• Meta: {SEO_RULES['meta_min']}–{SEO_RULES['meta_max']} chars
• Word Count: {SEO_RULES['min_word_count']}+
• H2 Sections: {SEO_RULES['min_h2']}+
• H3 Sections: {SEO_RULES['min_h3']}+
• FAQ Count: {SEO_RULES['min_faq']}+
• Internal Links: {SEO_RULES['min_internal_links']}+
• Mandatory Vedic Terms: {', '.join(SEO_RULES['mandatory_terms'])}
• Brand Mention: {SEO_RULES['brand_term']}
"""
