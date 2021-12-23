from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import math

import time

def get_html(url, wait_time):
  print('Initializing selenium and chrome driver...')
  driver = webdriver.Chrome(ChromeDriverManager().install())
  print('Scraping cragislist with selenium...')
  driver.get(url)
  time.sleep(wait_time)
  return driver.page_source
