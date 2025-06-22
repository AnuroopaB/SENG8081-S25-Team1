-- Check if the database exists, and create it if it doesn't
IF NOT EXISTS (
    SELECT name 
    FROM sys.databases 
    WHERE name = 'job_market_trends'
)
BEGIN
    CREATE DATABASE job_market_trends;
END
GO

-- Switch to the new database
USE job_market_trends;
GO

-- Table 1: Labour Force Stats
CREATE TABLE labour_force_stats (
    id INT IDENTITY(1,1) PRIMARY KEY,
    ref_date DATE,
    geo VARCHAR(100),
    dguid VARCHAR(50),
    characteristic VARCHAR(255),
    gender VARCHAR(50),
    age_group VARCHAR(100),
    statistic VARCHAR(100),
    data_type VARCHAR(100),
    uom VARCHAR(100),
    uom_id INT,
    scalar_factor VARCHAR(50),
    scalar_id INT,
    coordinate VARCHAR(50),
    value DECIMAL(12,2),
	decimals INT
);

-- Table 2: Industry-Level Jobs
CREATE TABLE industry_jobs (
    id INT IDENTITY(1,1) PRIMARY KEY,
    ref_date INT,
    geo VARCHAR(100),
    dguid VARCHAR(50),
    labour_statistic VARCHAR(255),
    naics_code VARCHAR(255),
    uom VARCHAR(50),
    uom_id INT,
    scalar_factor VARCHAR(50),
    scalar_id INT,
    vector VARCHAR(50),
    coordinate VARCHAR(50),
    value BIGINT,
    status VARCHAR(50),
    symbol VARCHAR(10),
    terminated VARCHAR(10),
    decimals INT
);

CREATE TABLE job_postings (
    JobID BIGINT IDENTITY(1,1) PRIMARY KEY,
    ApplicationsCount NVARCHAR(100),
    CompanyID NVARCHAR(50),
    CompanyName NVARCHAR(255),
    ContractType NVARCHAR(50),
    Description NVARCHAR(MAX),
    ExperienceLevel NVARCHAR(100),
    Location NVARCHAR(255),
    PostedTime NVARCHAR(100),
    PublishedAt DATE,
    Salary NVARCHAR(50),
    Sector NVARCHAR(255),
    Title NVARCHAR(255),
    WorkType NVARCHAR(100)
);

select * from job_postings;
