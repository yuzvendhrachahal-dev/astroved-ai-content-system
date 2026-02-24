import re
from services.openai_service import generate_content
from services.rag_engine import retrieve_recommendations
from services.link_mapper import auto_link_content
from utils.prompts import build_generation_prompt


# ----------------------------------------------------------
# CLEAN CONTENT
# ----------------------------------------------------------

def clean_generated_content(content: str):
    content = re.sub(r"\n{3,}", "\n\n", content)
    return content.strip()


# ----------------------------------------------------------
# REMOVE LINKS FROM TITLE
# ----------------------------------------------------------

def remove_links_from_title(content: str):
    lines = content.split("\n")
    if lines and lines[0].startswith("# "):
        lines[0] = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", lines[0])
    return "\n".join(lines)


# ----------------------------------------------------------
# REMOVE FAQ FOR ARTICLES
# ----------------------------------------------------------

def remove_faq_section(content: str):
    return re.sub(
        r"## Frequently Asked Questions.*",
        "",
        content,
        flags=re.DOTALL
    )


# ----------------------------------------------------------
# ENFORCE 5 FAQ WITH ANSWERS FOR BLOG
# ----------------------------------------------------------

def enforce_blog_faq(content: str):

    if "## Frequently Asked Questions" not in content:
        return content

    parts = content.split("## Frequently Asked Questions")

    body = parts[0]
    faq_block = parts[1]

    questions = re.findall(r"\d+\.\s*(.*?)\n(.*?)(?=\n\d+\.|\Z)", faq_block, re.DOTALL)

    final_faq = "\n## Frequently Asked Questions\n\n"

    for i, (q, a) in enumerate(questions[:5], 1):
        final_faq += f"{i}. {q.strip()}\n{a.strip()}\n\n"

    return body + final_faq


# ----------------------------------------------------------
# FORCE RECOMMENDATIONS (ALL TABS)
# ----------------------------------------------------------

def inject_recommendations(content: str, topic: str):

    # Try strong semantic match first
    recommendations = retrieve_recommendations(topic, top_k=5, threshold=0.80)

    # Fallback: if empty, take first 5 metadata entries
    if not recommendations:
        recommendations = retrieve_recommendations("pooja homa festival", top_k=5, threshold=1.0)

    if not recommendations:
        return content

    section = "\n\n## Recommended Poojas & Homas\n\n"

    for item in recommendations:
        title = item.get("title")
        url = item.get("url")

        if title and url:
            section += f"- [{title}]({url})\n"

    return content + section


# ----------------------------------------------------------
# OPTIMIZE EXISTING
# ----------------------------------------------------------

def optimize_existing_content(data, content_type="blog"):

    seo_keyword = data.get("title", "").strip()

    base_prompt = f"""
Rewrite and enhance this Vedic astrology content.

STRICT:
- 1500–1800 words
- The H1 MUST contain this exact SEO keyword:
  "{seo_keyword}"
- Do NOT create generic promotional titles
- Title must be search-intent driven
- Structured using # ## ###
"""

    if content_type == "blog":
        base_prompt += "\n- Exactly 5 FAQs with answers"
    else:
        base_prompt += "\n- Do NOT include FAQ section under any condition"

    base_prompt += f"\n\nOriginal Content:\n{data['content'][:5000]}"

    content = generate_content(base_prompt)

    content = clean_generated_content(content)
    content = auto_link_content(content)
    content = remove_links_from_title(content)

    if content_type == "article":
        content = re.sub(
            r"(##\s*Frequently Asked Questions.*?)(?=\n##|\Z)",
            "",
            content,
            flags=re.DOTALL | re.IGNORECASE
        )
    else:
        content = enforce_blog_faq(content)

    content = inject_recommendations(content, seo_keyword)

    return content

# ----------------------------------------------------------
# GENERATE NEW
# ----------------------------------------------------------

def generate_phase2_content(topic, date=None, optional_field=None, content_type="blog"):

    prompt = build_generation_prompt(topic, date, optional_field, content_type)

    content = generate_content(prompt)

    content = clean_generated_content(content)
    content = auto_link_content(content)
    content = remove_links_from_title(content)

    if content_type == "article":
        content = remove_faq_section(content)
    else:
        content = enforce_blog_faq(content)

    content = inject_recommendations(content, topic)

    return content