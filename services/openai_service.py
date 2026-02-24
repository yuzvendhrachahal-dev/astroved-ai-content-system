from openai import OpenAI
import os
from dotenv import load_dotenv
import re

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def enforce_indian_terminology(content: str):

    replacements = {
        "Puja": "Pooja",
        "puja": "pooja",
        "Lord ": "",
        "Lord": "",
        "Hindu god": "Vedic Deity",
        "Hindu gods": "Vedic Deities",
        "God Krishna": "Sri Krishna",
        "God Shiva": "Sri Shiva",
        "God Vishnu": "Sri Vishnu",
        "Lord Krishna": "Sri Krishna",
        "Lord Shiva": "Sri Shiva",
        "Lord Vishnu": "Sri Vishnu",
    }

    for old, new in replacements.items():
        content = content.replace(old, new)

    # Remove accidental slug exposure like .aspx
    content = re.sub(r"\.aspx", "", content)

    return content


def generate_content(prompt: str):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a senior Vedic astrology content specialist writing for AstroVed.\n\n"
                    "STRICT REQUIREMENTS:\n"
                    "- 1600–2000 words\n"
                    "- Indian terminology only\n"
                    "- Do NOT use the word 'Lord'\n"
                    "- Use Sri instead of Lord\n"
                    "- Use Pooja not Puja\n"
                    "- No Western astrology references\n"
                    "- No slug\n"
                    "- No URL path\n"
                    "- No .aspx\n"
                    "- Structured with Markdown headings\n"
                    "- Devotional yet authoritative tone\n"
                    "- Production-ready output only\n"
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.6,
        max_tokens=2000
    )

    content = response.choices[0].message.content

    content = enforce_indian_terminology(content)

    return content


def get_embedding(text: str):

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding