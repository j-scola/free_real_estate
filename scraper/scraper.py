
import time

from scrape_multiple_pages import scrape_multiple_pages
from parse_craigslist_search_results import parse_craigslist_search_results
from save_craigslist_result_page import save_craigslist_motorcycles
from cleanup import cleanup_data


def run_continuously(function, frequency_minutes, run_count): 
  count = run_count
  while count > 0:
    run_count -= 1
    print(f'Waiting {frequency_minutes} minutes... ({count} runs remaining)')
    time.sleep(frequency_minutes * 60)


if __name__ == '__main__':
  scrape_multiple_pages('https://sfbay.craigslist.org', '/d/motorcycles-scooters/search/mca')

  # with open('craigslist-motorcycles.html', 'r') as html:
  #   parse_craigslist_search_results(html.read())
  
  # cleanup_data()

