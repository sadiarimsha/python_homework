from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://owasp.org/www-project-top-ten/")

# Follow the link on the assigned page to reach the real Top 10 list
top_ten_link = driver.find_element(By.LINK_TEXT, 'OWASP Top Ten 2025')
top_ten_url = top_ten_link.get_attribute('href')
driver.get(top_ten_url)

# Find the list of 10 vulnerabilities and collect title + link for each
top_ten = driver.find_element(By.XPATH, '//h3[@id = "top-102025-list"]')
results = []

# Data scraping
sibling_div = top_ten.find_element(By.XPATH,'following-sibling::ol')
findings = sibling_div.find_elements(By.XPATH, './/a')
for find in findings:
    vulnerability = {}
    vulnerability['Title'] = find.text.strip()
    vulnerability['Link'] = find.get_attribute("href")
    results.append(vulnerability)

# Step 1: print the list to confirm the data is correct
print(results)

# Step 2: write the confirmed data out to a CSV file
df = pd.DataFrame(results)
print(df)

driver.quit()

# Write results to CSV
df.to_csv('owasp_top_10.csv', sep=',', index=False, header=True, encoding=None)
