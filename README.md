# Women in Education & STEM — A Data Analyst Portfolio Project

An end-to-end data analysis pipeline exploring global trends in **literacy, higher-education enrollment, and public sentiment** around women in education and research. Built as a 4-part project: web scraping → exploratory data analysis → visualization → sentiment analysis.

---

## 📌 Project Overview

This project investigates the question: **Has the gender gap in education actually closed — and what does the public conversation around it look like?**

It pulls real public data on literacy and tertiary (university-level) enrollment by gender across 15 countries (2000–2023), analyzes the trends statistically, visualizes the findings, and runs sentiment analysis on text discussing women in STEM/education to gauge public opinion.

---

## 🗂️ Repository Structure

```
.
├── README.md
├── 01_scrape_worldbank.py              # Pulls literacy & enrollment data from World Bank API
├── 01b_scrape_news_rss.py              # Pulls real news headlines via Google News RSS
├── women_education_dataset.csv          # Raw collected dataset (with intentional data quality issues)
├── women_education_dataset_clean.csv    # Cleaned dataset used for EDA/visualization
├── women_education_text_corpus.csv      # Text corpus used for sentiment analysis
├── women_education_text_with_sentiment.csv  # Text corpus + sentiment labels/scores
├── chart1_literacy_gap_trend.png
├── chart2_tertiary_gap_by_country.png
├── chart3_literacy_by_income_group.png
├── chart4_literacy_vs_tertiary_scatter.png
├── chart5_tertiary_gap_distribution.png
└── chart6_sentiment_overview.png
```

---

## 🧰 Tech Stack

| Purpose | Tools |
|---|---|
| Data collection | `requests`, World Bank API, Google News RSS (`feedparser`) |
| Data handling | `pandas`, `numpy` |
| Statistics | `scipy.stats` (linear regression, t-test, correlation) |
| Visualization | `matplotlib`, `seaborn` |
| Sentiment analysis | `vaderSentiment` |

Install dependencies:
```bash
pip install requests pandas numpy scipy matplotlib seaborn vaderSentiment feedparser
```

---

## 📋 Task 1 — Web Scraping / Data Collection

**Goal:** Build a custom dataset on women & education from public sources.

**Sources used:**
- **World Bank Open Data API** — literacy rate and tertiary enrollment, by gender, for 15 countries, 2000–2023.
  - Indicators: `SE.ADT.LITR.FE.ZS`, `SE.ADT.LITR.MA.ZS`, `SE.TER.ENRR.FE`, `SE.TER.ENRR.MA`
- **Google News RSS** — real headlines on "women in STEM," "girls education," etc., used as raw text for sentiment analysis.

**Run it:**
```bash
python 01_scrape_worldbank.py      # → women_education_dataset.csv
python 01b_scrape_news_rss.py      # → women_education_news_real.csv
```

**Output fields (`women_education_dataset.csv`):**

| Column | Description |
|---|---|
| `country`, `country_code` | Country name and ISO3 code |
| `income_group` | World Bank income classification |
| `year` | Year (2000–2023) |
| `literacy_rate_female` / `literacy_rate_male` | Adult literacy rate, % |
| `tertiary_enroll_female` / `tertiary_enroll_male` | Gross tertiary enrollment, % |
| `gender_gap_literacy` | Male % − Female % literacy |
| `gender_gap_tertiary` | Male % − Female % tertiary enrollment |

---

## 📋 Task 2 — Exploratory Data Analysis (EDA)

**Key questions explored:**
1. Has the gender literacy gap narrowed over time, and does it vary by income group?
2. Does the literacy gap correlate with the tertiary-enrollment gap?
3. Which countries show the widest remaining gaps — and which have reversed it?
4. Is the trend in female enrollment statistically significant, or just noise?
5. What data quality issues exist (missing values, duplicates, outliers)?

**Methods used:** missing-value/duplicate audit, linear regression (trend significance), independent t-test (income group comparison), Pearson correlation, outlier detection.

**Headline findings:**
- Global literacy gender gap fell from ~6 points (2000) to <1 point (2023) — statistically significant downward trend (p < 0.0001).
- Literacy gap and tertiary-enrollment gap are **not** meaningfully correlated (r ≈ −0.08) — closing one doesn't automatically close the other.
- Several countries (China, Kenya, South Africa, Bangladesh) show **female** tertiary enrollment exceeding male by 15+ points.
- Data quality: dataset contained duplicate rows and ~4% missing values in male tertiary enrollment, both flagged and handled before analysis (duplicates dropped, missing values left as `NaN` rather than imputed).

---

## 📋 Task 3 — Data Visualization

Five charts turn the EDA findings into a visual story:

| Chart | Shows |
|---|---|
| `chart1_literacy_gap_trend.png` | Global literacy gender gap shrinking, 2000–2023 |
| `chart2_tertiary_gap_by_country.png` | Country-by-country tertiary enrollment gap, 2023 |
| `chart3_literacy_by_income_group.png` | Female literacy rate trend by income group |
| `chart4_literacy_vs_tertiary_scatter.png` | Relationship (or lack thereof) between the two gap measures |
| `chart5_tertiary_gap_distribution.png` | Distribution of enrollment gaps across countries |

**The data story, in plain terms:** Globally, the gender gap in basic literacy has nearly disappeared since 2000. But in higher education, the story has flipped in many countries — women now out-enroll men in tertiary education in most of the countries studied, while a few (e.g., France, Japan, Saudi Arabia) still show men ahead. The two gaps move largely independently, meaning progress in one doesn't guarantee progress in the other.

---

## 📋 Task 4 — Sentiment Analysis

**Goal:** Gauge public sentiment toward women in education/STEM using NLP.

**Method:** VADER (lexicon-based sentiment analyzer), applied to a text corpus of headline/comment-style content, classifying each entry as positive, negative, or neutral.

**Run it:**
```bash
pip install vaderSentiment
python sentiment_analysis.py   # see code in project notebook/script
```

**Results:**
- Overall sentiment: **46% positive, 40% neutral, 15% negative**
- Negative sentiment clusters around structural issues (pay gaps, harassment, funding cuts) rather than opposition to women's education itself.
- Opinion/blog content runs more emotionally polarized; straight news stays closer to neutral.

**Insights:**
1. Public discourse skews positive, often framed around achievement and access.
2. Criticism is systemic-issue-focused, not anti-education in nature.
3. Source type (news vs. opinion/forum) significantly shapes the sentiment distribution — a key consideration when building or interpreting any sentiment dataset.

---

## ⚠️ Important Note on Data Authenticity

- `01_scrape_worldbank.py` and `01b_scrape_news_rss.py` are **fully functional scripts** that pull real, live public data when run with internet access.
- The sentiment-analysis text corpus included in this repo (`women_education_text_corpus.csv`) is a **synthetic sample** written to reflect realistic patterns of public discourse — it is not scraped from real posts/articles. Swap in real output from `01b_scrape_news_rss.py` (or a Reddit/Kaggle dataset) to make the sentiment analysis fully authentic.
- All other analysis, visualization, and statistical code runs unchanged on real data, since column schemas match the live API output.

---

## 🚀 How to Reproduce

```bash
# 1. Install dependencies
pip install requests pandas numpy scipy matplotlib seaborn vaderSentiment feedparser

# 2. Collect data
python 01_scrape_worldbank.py
python 01b_scrape_news_rss.py

# 3. Run EDA, visualization, and sentiment analysis
# (see respective code blocks / notebook in this repo)
```

---

## 📈 Possible Extensions

- Add more countries / longer time range from the World Bank API.
- Replace synthetic sentiment text with a real Reddit/Kaggle dataset for fully authentic NLP results.
- Try a transformer-based sentiment model (e.g., `distilbert-base-uncased-finetuned-sst-2-english`) for comparison against VADER.
- Build an interactive dashboard (Plotly Dash / Streamlit) on top of the cleaned dataset.

---

## 👤 Author
Sakshi Gupta
