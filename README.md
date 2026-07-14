# 🪐 AstroVed AI Content System

An enterprise-grade AI-powered content generation and SEO optimization system built for **AstroVed** using **Python**, **OpenAI GPT-4o**, **Streamlit**, and modern AI engineering practices.

The application assists the digital marketing team by automatically generating and optimizing Vedic astrology blogs, festival pages, and spiritual content while following modern SEO standards, maintaining AstroVed's brand tone, and reducing manual content creation effort.

The system supports both enhancing existing AstroVed pages and generating new production-ready articles with AI-powered validation.

---

# 🚀 Features

## Phase 1 – Existing Content Optimization

- Scrape existing AstroVed blog pages
- Analyze content structure and writing style
- Rewrite and optimize content using AI
- Improve readability and content depth
- Preserve devotional and Indian writing tone
- Generate production-ready SEO content
- AI-powered SEO validation report

---

## Phase 2 – New Content Generation

- Generate new Vedic astrology articles
- Festival blog generation
- Spiritual event pages
- Astrology educational articles
- FAQ generation
- Production-ready article generation
- AI-powered SEO validation report

---

## SEO Automation

- SEO optimized article generation
- Search intent optimization
- Primary & secondary keyword integration
- Semantic heading hierarchy
- FAQ generation
- Meta description generation
- SEO title optimization
- Internal linking support
- Indian terminology enforcement
- 2025–2026 SEO best practices

---

## AI Features

- OpenAI GPT-4o powered content generation
- Prompt engineered content workflow
- AI-assisted content enhancement
- Modular prompt architecture
- Context-aware article generation
- Production-ready validation workflow

---

# 🏗 Architecture

```text
                     +-------------------------+
                     |     Streamlit UI        |
                     +------------+------------+
                                  |
                                  |
                           User Inputs
                                  |
         +------------------------+-----------------------+
         |                                                |
         ▼                                                ▼
 Phase 1 - Existing Page                     Phase 2 - New Content
      Optimization                              Generation
         |                                                |
         ▼                                                ▼
 Existing Page Scraper                     Prompt Builder
         |                                                |
         ▼                                                ▼
  Content Optimizer ----------------------> OpenAI GPT-4o
         |                                                |
         +------------------------+-----------------------+
                                  |
                                  ▼
                         SEO Validation Engine
                                  |
                                  ▼
                      Production Ready Content
```

---

# 📂 Project Structure

```text
AI-CONTENT-GEN/
│
├── app.py
├── demo.py
├── requirements.txt
├── README.md
├── .env
│
├── data/
│
├── services/
│   ├── scraper.py
│   ├── optimizer.py
│   ├── openai_service.py
│   ├── seo_analyzer.py
│   ├── seo_validator.py
│
├── utils/
│   ├── prompts.py
│   └── seo_rules.py
│
└── venv/
```

---

# ⚙️ Tech Stack

## Backend

- Python 3.11
- Streamlit
- Requests
- BeautifulSoup4
- Python-dotenv

---

## AI

- OpenAI GPT-4o
- OpenAI Embeddings (RAG Ready)
- Prompt Engineering

---

## Web Scraping

- Requests
- BeautifulSoup
- HTML Parsing

---

## SEO

- Custom SEO Validation Engine
- Keyword Optimization
- Search Intent Optimization
- Readability Validation
- FAQ Generation

---

## Future AI Enhancements

- ChromaDB (RAG)
- Semantic Service Recommendation
- OpenAI Embeddings
- Context-aware Retrieval

---

# 🧠 System Workflow

## Phase 1 – Existing Page Optimization

```
User URL
      │
      ▼
Scrape AstroVed Page
      │
      ▼
Extract Content
      │
      ▼
AI Content Enhancement
      │
      ▼
SEO Validation
      │
      ▼
Production Ready Article
```

---

## Phase 2 – New Content Generation

```
Event Name
      │
      ▼
Prompt Builder
      │
      ▼
OpenAI GPT
      │
      ▼
Generate Production Article
      │
      ▼
SEO Validation
      │
      ▼
Production Ready Content
```

---

# 📊 SEO Rules Applied

The application follows modern SEO writing practices inspired by current industry standards.

### Content Quality

- 1500–1600 word articles
- Helpful and informative content
- Human-readable writing style
- Indian terminology and devotional tone

### Search Optimization

- Primary keyword targeting
- Secondary keyword variations
- Search intent optimization
- Semantic keyword placement
- FAQ optimization
- Featured snippet readiness

### Technical SEO

- SEO-friendly title
- Meta description generation
- Heading hierarchy (H1 → H2 → H3)
- Internal linking support
- Brand consistency
- E-E-A-T focused structure

---

# ⚡ Performance Optimizations

- Modular service architecture
- Prompt engineering
- Optimized OpenAI requests
- Reusable scraping service
- Production-ready validation engine
- Separation of business logic
- Scalable project structure

---

# 📌 Future Enhancements

- Retrieval-Augmented Generation (RAG)
- ChromaDB integration
- Semantic service recommendation engine
- OpenAI Embedding search
- Automatic AstroVed service mapping
- Bulk content generation
- Editorial review workflow
- CMS integration
- FastAPI backend deployment

---

# ▶️ Running Locally

## Clone Repository

```bash
git clone https://github.com/yuzvendhrachahal-dev/astroved-ai-content-system.git

cd astroved-ai-content-system
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create a `.env` file

```env
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
```

---

## Run Application

```bash
streamlit run app.py
```

---

# 🧠 AI Engineering Concepts Demonstrated

- AI Application Development
- Prompt Engineering
- OpenAI API Integration
- Content Generation Systems
- Web Scraping
- SEO Automation
- Modular Python Architecture
- AI Workflow Design
- Production-ready Validation
- Streamlit Application Development
- Context-aware Content Generation
- RAG-ready Architecture

---

# 👨‍💻 Author

**Nivash R N**

- GitHub: https://github.com/RNNivash
- LinkedIn: https://linkedin.com/in/nivash-r-n
- Portfolio: https://rnnivash.github.io/My_Port/
