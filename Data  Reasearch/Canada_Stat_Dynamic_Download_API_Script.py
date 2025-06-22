from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from datetime import datetime

# Set download directory
download_dir = os.path.join(os.getcwd(), "downloads")

# Configure Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # remove headless to see browser
options.add_argument("--window-size=1920,1080")
prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "directory_upgrade": True,
    "safebrowsing.enabled": True
}
options.add_experimental_option("prefs", prefs)

# Path to chromedriver
CHROME_PATH = 'C:\\Program Files (x86)\\chromedriver-win64\\chromedriver.exe'
driver = webdriver.Chrome(service=Service(CHROME_PATH), options=options)

# Open StatsCan table
url = "https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410028701"
driver.get(url)

# Wait for "Customize table" to be clickable
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Customize table"))).click()

# Wait for period drop-down to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "periods-from")))
Select(driver.find_element(By.ID, "periods-from")).select_by_visible_text("January 2020")
# Let "to" remain as default (Latest)

# Click Apply button
driver.find_element(By.ID, "applyChangesButton").click()

# Wait for data to load
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "download-button-container")))

# Click Download > CSV
driver.find_element(By.ID, "download-button-container").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'CSV')]"))).click()

# Wait for download to complete
time.sleep(15)

# Rename downloaded file
csv_file = max([os.path.join(download_dir, f) for f in os.listdir(download_dir)], key=os.path.getctime)
new_name = f"statcan_job_vacancy_{datetime.now().strftime('%Y%m%d')}.csv"
os.rename(csv_file, os.path.join(download_dir, new_name))

print(f"Downloaded: {new_name} in {download_dir}")

# Close browser
driver.quit()
