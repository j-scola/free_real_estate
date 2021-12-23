from logging import error
from bs4 import BeautifulSoup
import math
import time

from get_webpage_html import get_html
from parse_craigslist_search_results import parse_craigslist_search_results

def scrape_multiple_pages(base_url, intitial_path):
  html = get_html(f'{base_url}{intitial_path}', 5)  
  soup = BeautifulSoup(html, 'lxml')
  page_data = cl_get_results_count_data(soup)
  iterations = math.ceil(int(page_data['total_results_count']) / int(page_data['page_display_count']))
  first_iteration = True

  print('Obtaining HTML markdown for craigslist url')
  while iterations > 0:
    print(page_data)
    if not first_iteration:
      path = page_data['next_page_link']
      html = get_html(f'{base_url}{path}', 10)
      soup = BeautifulSoup(html, 'lxml')
      page_data = cl_get_results_count_data(soup)
 
    else: 
      first_iteration = False
    
    # parse and save html data to file system
    parse_craigslist_search_results(html)
    
    iterations -= 1
    print(f'{iterations} pages remaining...')    

    
def cl_get_results_count_data(soup):
  try: 
    pagination = soup.find('div', class_="paginator")
    total_results_count = pagination.find('span', class_="totalcount").text
    page_display_count = pagination.find('span', class_="button pagenum").find('span', class_="rangeTo").text
    next_page_link = pagination.find('a', class_="button next").attrs['href']
  except AttributeError as err:
    print(err)
    time.sleep(10)
  
  return {
    'total_results_count': total_results_count,
    'page_display_count': page_display_count,
    'next_page_link': next_page_link
  }
  
