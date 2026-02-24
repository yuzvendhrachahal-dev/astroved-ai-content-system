def build_generation_prompt(event, date, optional_field=None, content_type="blog"):

    if optional_field and optional_field.strip():
        context_instruction = f"Additional Context: {optional_field}"
    else:
        context_instruction = "Include traditional Indian Pooja and Homa details."

    base = f"""
Create a high-impact, campaign-style Vedic astrology article for AstroVed.

STRICT REQUIREMENTS:

TITLE RULES (VERY IMPORTANT):

- The H1 must be powerful and event-focused.
- Use strong campaign-style wording.
- Title may be FULL CAPS or partially capitalized.
- Keep it authoritative and devotional.
- Must clearly contain the Event/Topic name.
- No generic blog-style titles.
- No slugs.
- No URLs.
- No .aspx.
- No hyperlink in title.

Examples of style:
- LUNAR ECLIPSE 2026: POWERFUL REMEDIES & COSMIC TRANSFORMATION
- NAVAGRAHA YEARLONG PROGRAM
- RARE 5-PLANET STELLIUM IN AQUARIUS
- ASHTA AISHWARYA PROGRAM: MANIFEST EIGHT TYPES OF WEALTH
- GRAND NAVA NARASIMHA INVOCATION

CONTENT STRUCTURE:

- 1500–1800 words
- Structured using:
    # H1 (exactly one)
    ## H2
    ### H3
- Deep spiritual insights
- Zodiac-wise benefits
- Clear ritual guidance (Pooja, Homa, Sankalpa, Offerings)
- Devotional yet authoritative tone
- Indian terminology only (Pooja, Homa, Graha, Nakshatra, Dasha)
- Do NOT use the word "Lord"
- Use Sri instead of Lord
- No Western astrology references
- No filler content
- Production-ready output

Event/Topic: {event}
Date: {date}
{context_instruction}
"""

    if content_type == "blog":
        base += """

BLOG REQUIREMENTS:

- Include a mandatory FAQ section
- Exactly 5 detailed Q&A
- FAQ section must start strictly with:
  ## Frequently Asked Questions
"""
    else:
        base += """

ARTICLE REQUIREMENTS:

- Do NOT include FAQ section under any condition
"""

    base += """

Return only the final structured article in Markdown format.
"""

    return base
