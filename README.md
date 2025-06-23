# SENG8081-S25-Team1
## Contibutors
* Anuroopa Balachandran
* Bin Hu
* Ce Chen
* Xiaoman Yang

## Project
### Canadian Job Market Trends Analaysis 

#### Abstract
In today's dynamic economic landscape, understanding job market trends is critical for policymakers, businesses, and job seekers. This project outlines solution for analyzing Canadian job market trends by integrating real-time data from government APIs with curated historical datasets. The system tracks key metrics such as employment rates, industry growth, regional demand, and skill requirements to analyze and visualize employment trends, job posting dynamics, sectoral shifts, and unemployment patterns across Canadian provinces, with the goal of identifying economic signals, emerging industries, and potential indicators of recession or recovery.

#### Introduction
This project conducts a comprehensive analysis of Canada’s job market, focusing on employment trends, regional disparities, industry growth, and emerging skill demands. Objectives include:
* Identifying high-growth sectors and declining industries.
* Analyzing regional employment hotspots.
* Predicting future skill requirements using historical data.
* Building an interactive dashboard for policymakers and job seekers.

#### System Components
* Python Backend: Data ingestion, cleaning, and analysis.
* Real-Time API: Statistics Canada Labour Force Survey API.
* Historical Dataset: Government of Canada Open Data Portal archives and Kaggle dataset.
* Database: Microsoft SQL Server - Structured storage for time-series data.
* Dashboard: Tableau for visualization.

#### Data Research and Integration

##### Sources
* https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410028701
* https://open.canada.ca/data/dataset/a70fcb3b-9a57-4e10-8372-9016935fc5d9
* https://www.kaggle.com/datasets/arshkon/linkedin-job-postings

#### Data Collection

##### Purpose

- Cleaning datasets by fixing missing, null or error values.
- Standardize raw data formats for loading into the job_market_trends database.
- Maintain reproducibility and versioning of collected data files.

##### Approaches

1. Historical Data
    1. Download CSV/JSON datasets.
    2. Clean data using pandas.
    3. Load into SQL Server via pyodbc.

2. Real-Time Data
    1. Fetch data using API key and Python’s requests.
    2. Parse responses into structured tables.
    3. Merge with historical data using pandas/SQL.

#### Data Storage and Maintenance

Data Storage: Microsoft SQL Server

##### Schema: 

Database: job_market_trends
Tables: 
1. _labour_force_stats_: Labour force characteristics by region, gender, age group

2. _industry_jobs_: NAICS industry job counts across years and sectors

3. _job_postings_: Detailed job postings scraped from LinkedIn or Google Jobs

##### Maintenance Practices

✅ Ingestion Strategy
- Use `load_data.py` to insert or append CSV data to MySQL
- Column normalization and null checks handled before insert
- Timestamp columns converted appropriately

🔄 Update Schedule
- Monthly: Labour Force & Industry Jobs (from StatsCan, Open Canada)
- Daily/Weekly:Job postings via automated scraper
- Monthly archiving of API data.
- Automated backups.

🧹 Data Hygiene
- De-duplication using primary keys
- Missing values filled with defaults or flagged for review
- Normalization ensures analytical consistency

🛡️ Backups
- Weekly dump using `mysqldump` to `/backups/`
- Retain minimum 3 historical snapshots

### Next Phase Plan
- Merge all the scripts together and add automated testcases.
- Start with Data Quality
- Finalize on the visualizations required





