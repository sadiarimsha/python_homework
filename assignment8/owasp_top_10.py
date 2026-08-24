from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://owasp.org/Top10/2025/")

top_ten = driver.find_element(By.CSS_SELECTOR,'h3[id="top-102025-list"]')

results = []

sibling_div = top_ten.find_element(By.XPATH,'following-sibling::ol')
findings = sibling_div.find_elements(By.CSS_SELECTOR, 'a')
for find in findings:
    vulnerability = {}
    vulnerability['Title'] = find.text.strip()
    vulnerability['Link'] = find.get_attribute("href")
    results.append(vulnerability)
print(results)

df = pd.DataFrame(results)
print(df)

df.to_csv('owasp_top_10.csv', sep=',', index=False, header=True, encoding=None)
