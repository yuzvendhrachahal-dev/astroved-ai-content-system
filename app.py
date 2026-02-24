import streamlit as st
from datetime import date
from urllib.parse import urlparse
import re

from services.scraper import ContentScraper
from services.optimizer import (
    optimize_existing_content,
    generate_phase2_content
)
from services.seo_validator import validate_content
from utils.doc_exporter import markdown_to_docx
import os
APP_PASSWORD = os.getenv("APP_PASSWORD")

st.set_page_config(page_title="AstroVed AI Content System", layout="wide")

st.title("🪐 AstroVed AI Content System")

def check_password():
    def password_entered():
        if st.session_state["password"] == APP_PASSWORD:
            st.session_state["password_correct"] = True
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Enter Password", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Enter Password", type="password", on_change=password_entered, key="password")
        st.error("Incorrect Password")
        return False
    else:
        return True

if not check_password():
    st.stop()
    
tabs = st.tabs([
    "Optimize Existing Blog",
    "Generate New Blog",
    "Generate New Article",
    "Optimize Existing Article"
])


# ==========================================================
# Utility: Convert URL Slug to Proper Title
# ==========================================================
def url_to_filename(url):
    path = urlparse(url).path
    slug = path.rstrip("/").split("/")[-1]
    name = slug.replace("-", " ")
    name = re.sub(r"\.aspx$", "", name)
    return name.title()


# ==========================================================
# TAB 1 – OPTIMIZE EXISTING BLOG
# ==========================================================
with tabs[0]:

    st.header("SEO Enhancement – Existing Blog")

    blog_url = st.text_input(
        "AstroVed Blog URL",
        key="opt_blog_url"
    )

    col1, col2 = st.columns([2, 1])

    if col1.button("Optimize Blog", key="opt_blog_btn"):

        try:
            with st.spinner("Scraping and Enhancing Blog..."):

                scraper = ContentScraper()
                data = scraper.scrape(blog_url)

                if not data or not data.get("content"):
                    st.error("Failed to scrape content.")
                    st.stop()

                optimized = optimize_existing_content(data)
                validation = validate_content(optimized, content_type="blog")

                st.session_state.opt_blog_content = optimized
                st.session_state.opt_blog_validation = validation
                st.session_state.opt_blog_filename = url_to_filename(blog_url)

        except Exception as e:
            st.error(str(e))

    if "opt_blog_content" in st.session_state:

        doc_buffer = markdown_to_docx(st.session_state.opt_blog_content)

        col2.download_button(
            "📥 Download Word",
            doc_buffer,
            file_name=f"{st.session_state.opt_blog_filename}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

        st.success("Blog Optimized Successfully")

        st.markdown(st.session_state.opt_blog_content)
        st.markdown("---")
        st.markdown(st.session_state.opt_blog_validation)


# ==========================================================
# TAB 2 – GENERATE NEW BLOG
# ==========================================================
with tabs[1]:

    st.header("Generate New Blog")

    blog_topic = st.text_input(
        "Blog Topic",
        "Diwali 2026",
        key="new_blog_topic"
    )

    blog_date = st.date_input(
        "Event Date",
        date.today(),
        key="new_blog_date"
    )

    formatted_date = blog_date.strftime("%B %d, %Y")

    blog_context = st.text_area(
        "Optional Context",
        key="new_blog_context"
    )

    col1, col2 = st.columns([2, 1])

    if col1.button("Generate Blog", key="new_blog_btn"):

        try:
            with st.spinner("Generating Blog..."):

                content = generate_phase2_content(
                    blog_topic,
                    formatted_date,
                    blog_context,
                    content_type="blog"
                )

                validation = validate_content(content, content_type="blog")

                st.session_state.new_blog_content = content
                st.session_state.new_blog_validation = validation
                st.session_state.new_blog_filename = blog_topic.strip()

        except Exception as e:
            st.error(str(e))

    if "new_blog_content" in st.session_state:

        doc_buffer = markdown_to_docx(st.session_state.new_blog_content)

        col2.download_button(
            "📥 Download Word",
            doc_buffer,
            file_name=f"{st.session_state.new_blog_filename}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

        st.success("New Blog Generated Successfully")

        st.markdown(st.session_state.new_blog_content)
        st.markdown("---")
        st.markdown(st.session_state.new_blog_validation)


# ==========================================================
# TAB 3 – GENERATE NEW ARTICLE
# ==========================================================
with tabs[2]:

    st.header("Generate New Article")

    article_topic = st.text_input(
        "Article Topic",
        "Saturn Transit Effects",
        key="new_article_topic"
    )

    article_context = st.text_area(
        "Optional Context",
        key="new_article_context"
    )

    col1, col2 = st.columns([2, 1])

    if col1.button("Generate Article", key="new_article_btn"):

        try:
            with st.spinner("Generating Article..."):

                content = generate_phase2_content(
                    article_topic,
                    None,
                    article_context,
                    content_type="article"
                )

                validation = validate_content(content, content_type="article")

                st.session_state.new_article_content = content
                st.session_state.new_article_validation = validation
                st.session_state.new_article_filename = article_topic.strip()

        except Exception as e:
            st.error(str(e))

    if "new_article_content" in st.session_state:

        doc_buffer = markdown_to_docx(st.session_state.new_article_content)

        col2.download_button(
            "📥 Download Word",
            doc_buffer,
            file_name=f"{st.session_state.new_article_filename}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

        st.success("New Article Generated Successfully")

        st.markdown(st.session_state.new_article_content)
        st.markdown("---")
        st.markdown(st.session_state.new_article_validation)


# ==========================================================
# TAB 4 – OPTIMIZE EXISTING ARTICLE
# ==========================================================
with tabs[3]:

    st.header("SEO Enhancement – Existing Article")

    article_url = st.text_input(
        "AstroVed Article URL",
        key="opt_article_url"
    )

    col1, col2 = st.columns([2, 1])

    def remove_faq_section(content):
        # Remove FAQ block
        content = re.sub(
            r"(##\s*Frequently Asked Questions.*?)(?=\n##|\Z)",
            "",
            content,
            flags=re.DOTALL | re.IGNORECASE
        )

        # Remove plain "FAQ Section"
        content = re.sub(
            r"(FAQ\s*Section.*?)(?=\n##|\Z)",
            "",
            content,
            flags=re.DOTALL | re.IGNORECASE
        )

        return content.strip()


    if col1.button("Optimize Article", key="opt_article_btn"):

        try:
            with st.spinner("Scraping and Enhancing Article..."):

                scraper = ContentScraper()
                data = scraper.scrape(article_url)

                if not data or not data.get("content"):
                    st.error("Failed to scrape content.")
                    st.stop()

                #  Only call optimizer ONCE
                optimized = optimize_existing_content(data, content_type="article")

                # FORCE REMOVE FAQ FOR TAB 4
                optimized = remove_faq_section(optimized)

                validation = validate_content(
                    optimized,
                    content_type="article"
                )

                st.session_state.opt_article_content = optimized
                st.session_state.opt_article_validation = validation
                st.session_state.opt_article_filename = url_to_filename(article_url)

        except Exception as e:
            st.error(str(e))

    if "opt_article_content" in st.session_state:

        doc_buffer = markdown_to_docx(st.session_state.opt_article_content)

        col2.download_button(
            "📥 Download Word",
            doc_buffer,
            file_name=f"{st.session_state.opt_article_filename}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

        st.success("Article Optimized Successfully")

        st.markdown(st.session_state.opt_article_content)
        st.markdown("---")
        st.markdown(st.session_state.opt_article_validation)