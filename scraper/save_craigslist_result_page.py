from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

def save_craigslist_motorcycles():
  print('Initializing selenium and chrome driver...')
  driver = webdriver.Chrome(ChromeDriverManager().install())
  print('Scraping cragislist with selenium...')
  driver.get(f'https://sfbay.craigslist.org/d/motorcycles-scooters/search/mca')
  
  time.sleep(3) 
   
  html = driver.page_source
  
  with open('craigslist-motorcycles.html', 'a') as f:
    f.write(html)
    f.close()