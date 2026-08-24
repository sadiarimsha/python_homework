
#Task 3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import csv
import json

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

search_results = driver.find_elements(By.CSS_SELECTOR,'li.row.cp-search-result-item')
if len(search_results) > 0:
    print(len(search_results))

results = []

for search in search_results:
    book = {}
    search_title = search.find_element(By.CSS_SELECTOR,'span.title-content')
    book['Title'] = search_title.text

    search_author = [(author_element.text) for author_element in search.find_elements(By.CSS_SELECTOR,'a.author-link')]
    if len(search_author) > 1:
        book['Author'] = ';'.join(search_author)
    else:
        book['Author'] = search_author[0]

    search_format = search.find_element(By.CSS_SELECTOR,'div.cp-format-info span.display-info-primary')
    book['Format-Year'] = search_format.text
    
    results.append(book)

df = pd.DataFrame(results)
print(df)

# Task 4
df.to_csv('get_books.csv', sep=',', index=False, header=True, encoding=None)

with open('get_books.json', 'w') as json_file:
    json.dump(results, json_file, indent=4)
