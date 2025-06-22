import pyodbc
import pandas as pd
import numpy as np
from datetime import datetime
import os
import logging
from tqdm import tqdm

# Configure logging
logging.basicConfig(filename='data_import.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Database connection
def create_db_connection():
    """Create and return a database connection"""
    conn_str = (
            'DRIVER={ODBC Driver 17 for SQL Server};'
            r'SERVER=ROOZ\ANUSQL;'
            'DATABASE=job_market_trends;'
            'Trusted_Connection=yes;'
        )
    
    try:
        conn = pyodbc.connect(conn_str)
        logging.info("Successfully connected to database")
        return conn
    except pyodbc.Error as e:
        logging.error(f"Database connection failed: {str(e)}")
        raise

def insert_labour_force_stats(conn, file_path):
    """Insert data from CSV to labour_force_stats table"""
    try:
        # Read and clean data
        df = pd.read_csv(file_path)
        
        # Convert ref_date to proper date format (assuming YYYY-MM format)
        if 'ref_date' in df.columns:
            df['ref_date'] = pd.to_datetime(df['ref_date'] + '-01', errors='coerce')
        
        # Prepare data
        records = [tuple(x) for x in df.to_records(index=False)]
        
        # SQL query
        query = """
        INSERT INTO labour_force_stats (
            ref_date, geo, dguid, characteristic, gender, age_group, 
            statistic, data_type, uom, uom_id, scalar_factor, scalar_id, 
            coordinate, value
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        
        # Insert data
        with conn.cursor() as cursor:
            cursor.fast_executemany = True
            for i in tqdm(range(0, len(records), 1000), desc="Inserting Labour Data"):
                batch = records[i:i+1000]
                cursor.executemany(query, batch)
            conn.commit()
        
        logging.info(f"Successfully inserted {len(records)} rows into labour_force_stats")
        return len(records)
    
    except Exception as e:
        logging.error(f"Error inserting labour data: {str(e)}")
        conn.rollback()
        return 0

def insert_industry_jobs(conn, file_path):
    """Insert data from CSV to industry_jobs table"""
    try:
        # Read and clean data
        df = pd.read_csv(file_path)
        
        # Prepare data
        records = [tuple(x) for x in df.to_records(index=False)]
        
        # SQL query
        query = """
        INSERT INTO industry_jobs (
            ref_date, geo, dguid, labour_statistic, naics_code, 
            uom, uom_id, scalar_factor, scalar_id, vector, coordinate, 
            value, status, symbol, terminated, decimals
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        
        # Insert data
        with conn.cursor() as cursor:
            cursor.fast_executemany = True
            for i in tqdm(range(0, len(records), 1000), desc="Inserting Industry Data"):
                batch = records[i:i+1000]
                cursor.executemany(query, batch)
            conn.commit()
        
        logging.info(f"Successfully inserted {len(records)} rows into industry_jobs")
        return len(records)
    
    except Exception as e:
        logging.error(f"Error inserting industry data: {str(e)}")
        conn.rollback()
        return 0

def insert_jobs(conn, file_path):
    """Insert data from CSV to jobs table"""
    try:
        print("started")
        # Read and clean data
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip().str.lower()
        # Convert 'publishedat' to proper date format
        if 'publishedat' in df.columns:
            try:
                df['publishedat'] = pd.to_datetime(df['publishedat'], errors='coerce')
            except Exception as e:
                logging.warning(f"Failed to convert 'publishedat': {str(e)}")

        # Prepare data
        records = [tuple(x) for x in df.to_records(index=False)]
        print("Record length:", len(records[0]))

        # SQL INSERT query for SQL Server
        query = """
        INSERT INTO job_postings (
            applicationscount, companyid, companyname, contracttype,
            description, experiencelevel, location, postedtime, publishedat,
            salary, sector, title, worktype
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        # Insert in batches
        with conn.cursor() as cursor:
            cursor.fast_executemany = True
            for i in tqdm(range(0, len(records), 1000), desc="Inserting JobPostings"):
                batch = records[i:i+1000]
                try:
                    cursor.executemany(query, batch)
                except Exception as e:
                    logging.error(f"Batch {i}-{i+len(batch)} failed: {e}")
                    print(f"Sample record: {batch[0]}")
            conn.commit()

        logging.info(f"Successfully inserted {len(records)} rows into JobPostings")
        return len(records)


    except Exception as e:
        logging.error(f"Error inserting job postings: {str(e)}")
        conn.rollback()
        return 0

def main():
    # CSV file paths
    labour_csv = 'labour_force_stats.csv'
    industry_csv = 'industry_jobs.csv'
    jobs_csv = 'CLEANED_jobs_canada.csv'
    
    # Create database connection
    try:
        conn = create_db_connection()
    except Exception as e:
        print(f"Critical error: Failed to connect to database. See logs for details.")
        return
    
    # Import data
    print("Starting data import process...")
    
    # Labour force stats
    if os.path.exists(labour_csv):
        print(f"\nImporting labour force data from {labour_csv}")
        count = insert_labour_force_stats(conn, labour_csv)
        print(f"Inserted {count} records into labour_force_stats")
    else:
        print(f"Warning: Labour data file not found - {labour_csv}")
    
    # Industry jobs
    if os.path.exists(industry_csv):
        print(f"\nImporting industry job data from {industry_csv}")
        count = insert_industry_jobs(conn, industry_csv)
        print(f"Inserted {count} records into industry_jobs")
    else:
        print(f"Warning: Industry data file not found - {industry_csv}")
    
    # Job postings
    if os.path.exists(jobs_csv):
        print(f"\nImporting job postings from {jobs_csv}")
        count = insert_jobs(conn, jobs_csv)
        print(f"Inserted {count} records into jobs")
    else:
        print(f"Warning: Jobs data file not found - {jobs_csv}")
    
    # Clean up
    conn.close()
    print("\nData import process completed!")

if __name__ == "__main__":
    main()