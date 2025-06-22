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

#### Data Research and Integration

##### Sources
* https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410028701
* https://open.canada.ca/data/dataset/a70fcb3b-9a57-4e10-8372-9016935fc5d9
* https://www.kaggle.com/datasets/ortizmacleod/employment-rate-canada
* https://www.kaggle.com/datasets/arshkon/linkedin-job-postings

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

Data Maintenance:

* Monthly archiving of API data.
* Automated backups.
