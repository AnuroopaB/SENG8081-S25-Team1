import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import datetime, timedelta

# Configure Chrome options
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--disable-infobars')
options.add_argument('--disable-extensions')

# Initialize WebDriver
driver = webdriver.Chrome(options=options)

job_titles_search_keywords = [
    "Data Scientist", "Data Analyst", "Data Engineer", 
    "Machine Learning Engineer", "Statistician", "Data Architect",
    "Business Intelligence Analyst", "Data Science Manager",
    "Big Data Engineer", "Quantitative Analyst"
]

locations = ['canada', 'vancouver', 'toronto', 'montreal', 
             'calgary', 'edmonton', 'ottawa', 'mississauga', 'winnipeg']

class JobListing:
    def __init__(self, title, company, description, job_type, 
                 location, job_id, salary, platform, posting_date):
        self.title = title
        self.company = company
        self.description = description
        self.location = location
        self.jobID = job_id
        self.jobType = job_type
        self.salary = salary
        self.platform = platform
        self.posting_date = posting_date

def get_google_url(position, location):
    search_string = position.replace(' ', '+')
    return f"https://www.google.com/search?q={search_string}+jobs+{location}&ibp=htl;jobs"

def get_job_id(url):
    if 'htidocid=' in url:
        return url.split('htidocid=')[1].split('&')[0]
    return None

def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
    time.sleep(0.5)

def get_listings(driver):
    return WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "PwjeAc"))
    )

def get_job_title(driver):
    return WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "KLsYvd"))
    ).text

def get_company_name(driver):
    return WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "nJlQNd"))
    ).text

def get_location(driver):
    return WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "sMzDkb"))
    )[-1].text

def get_job_type(driver):
    return WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "LL4CDc"))
    )[-1].text

def get_description(driver):
    try:
        # Try to expand description if "Show more" exists
        show_more = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "atHusc"))
        )
        show_more.click()
        time.sleep(0.5)
    except:
        pass
    
    return WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "HBvzbc"))
    ).text

def get_salary(job_item):
    try:
        return job_item.find_element(By.CLASS_NAME, "LL4CDc").text
    except:
        return 'Not specified'

def get_platform(job_item):
    try:
        return job_item.find_element(By.CLASS_NAME, "Qk80Jf").text.replace('via ', '')
    except:
        return 'Direct'

def get_posting_date(job_item):
    try:
        date_text = job_item.find_element(By.XPATH, './/span[contains(text()," ago")]').text
        num = int(date_text.split()[0])
        unit = date_text.split()[1]
        
        if 'day' in unit:
            delta = timedelta(days=num)
        elif 'hour' in unit:
            delta = timedelta(hours=num)
        elif 'minute' in unit:
            delta = timedelta(minutes=num)
        else:
            return datetime.now().strftime("%Y-%m-%d")
            
        return (datetime.now() - delta).strftime("%Y-%m-%d")
    except:
        return datetime.now().strftime("%Y-%m-%d")

def get_job_data(positions, locations):
    jobs = []
    for location in locations:
        for position in positions:
            print(f"Searching: {position} in {location}")
            driver.get(get_google_url(position, location))
            
            try:
                # Dismiss initial popup if exists
                WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Accept all']]"))
                ).click()
            except:
                pass
            
            time.sleep(2)  # Wait for results to load
            
            try:
                listings = get_listings(driver)
                print(f"Found {len(listings)} listings")
                
                for i, listing in enumerate(listings[:5]):  # Limit to 5 per search
                    print(f"Processing listing {i+1}/{len(listings)}")
                    scroll_to_element(driver, listing)
                    listing.click()
                    time.sleep(1)
                    
                    try:
                        title = get_job_title(driver)
                        company = get_company_name(driver)
                        location = get_location(driver)
                        job_type = get_job_type(driver)
                        description = get_description(driver)
                        job_id = get_job_id(driver.current_url)
                        salary = get_salary(listing)
                        platform = get_platform(listing)
                        posting_date = get_posting_date(listing)
                        
                        job = JobListing(
                            title, company, description, job_type,
                            location, job_id, salary, platform, posting_date
                        )
                        
                        jobs.append(job)
                        print(f"Added: {title} at {company}")
                    except Exception as e:
                        print(f"Error processing job: {str(e)}")
                        continue
            except Exception as e:
                print(f"Error getting listings: {str(e)}")
                continue
                
    return jobs

# Main execution
try:
    print("Starting job search...")
    job_listings = get_job_data(job_titles_search_keywords, locations)
    
    if job_listings:
        df = pd.DataFrame([vars(job) for job in job_listings])
        filename = f"google_jobs_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.csv"
        df.to_csv(filename, index=False)
        print(f"Saved {len(df)} jobs to {filename}")
    else:
        print("No jobs found")
        
except Exception as e:
    print(f"Critical error: {str(e)}")
finally:
    driver.quit()
    print("Browser closed")