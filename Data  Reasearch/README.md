## 📊 Data Research - Canadian Job Market Trends Analysis Project

This folder contains curated datasets collected by all the members for exploring the Canadian job market. The data serves as the foundation for modeling trends, demand forecasting, and dashboard visualizations in the `job_market_trends` system.

## 📁 Datasets Included

We have collected quite a lot of datasets from multiple sources, but after careful observation we filtered below datasets to use for our project.

#### 1. Statistics Canada - Table 14-10-0287-01: *https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410028701* 
**Description**: Monthly labour force characteristics for the Canadian population, covering data from January 2020 to present.  
*Canada_Stat_Dynamic_Download_API_Script.py is used to dynamically fetch data based on current date.* 

#### 2. Open Canada – Canadian Job Bank Industry Dataset: *https://open.canada.ca/data/dataset/a70fcb3b-9a57-4e10-8372-9016935fc5d9* 
**Description**: Industry-wise job statistics based on the NAICS system from 1997 onward.  

#### 3. Kaggle – LinkedIn Job Postings Dataset: *https://www.kaggle.com/datasets/arshkon/linkedin-job-postings*,  combined with real-time job search results.
**Description**: Aggregated job postings scraped from LinkedIn, including compensation details, work type, and location and direct search results using API calls.  
*Job_Posting_Dynamic_Download_API_Script.py is used to fetch realtime job search results.*

