## 🗄️ Data Storage and Maintenance - Canadian Job Market Trends Analysis Project

This folder documents the schema design, storage structure, and maintenance strategy for managing job market datasets in the job_market_trends MySQL database.

### Objectives

- Centralize and normalize raw and enriched job market data in a relational database
- Enable efficient querying and analysis via SQL and external tools (Tableau)
- Support continuous updates and integration of real-time data feeds

### Database: `job_market_trends`

This MySQL database hosts all the curated job market data. Tables were designed to maintain normalized structure, consistent field types, and support future scalability.

### 🗂️ Core Tables

*Schema_Creation_Script.sql* defines the schema for database job_market_trends and below tables:

1. `labour_force_stats`
- Labour force characteristics by region, gender, age group
- Source: Statistics Canada Table 14-10-0287-01

2. `industry_jobs`
- NAICS industry job counts across years and sectors
- Source: Open Canada Job Bank

3. `job_postings`
- Detailed job postings scraped from LinkedIn or Google Jobs
- Integrates with real time jib search results
- Source: Kaggle

### ⚙️ Maintenance Practices

#### ✅ Ingestion Strategy
- Use `load_data.py` to insert or append CSV data to MySQL
- Column normalization and null checks handled before insert
- Timestamp columns converted appropriately

#### 🔄 Update Schedule
- Monthly: Labour Force & Industry Jobs (from StatsCan, Open Canada)
- Daily/Weekly:Job postings via automated scraper

#### 🧹 Data Hygiene
- De-duplication using primary keys
- Missing values filled with defaults or flagged for review
- Normalization ensures analytical consistency

#### 🛡️ Backups
- Weekly dump using `mysqldump` to `/backups/`
- Retain minimum 3 historical snapshots

### 📤 Integration Points

- Data is used by:
  - _load_data.py_ for ingest
  - Dashboards for trends and forecasting
  - APIs or Streamlit app for real-time insights
