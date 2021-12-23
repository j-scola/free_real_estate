from bs4 import BeautifulSoup

def parse_craigslist_search_results(html):
  print('Parsing html file with Beautiful Soup...')
  soup = BeautifulSoup(html, 'lxml')
  li = soup.findAll('li', class_='result-row')
  with open('data/motorcycles.txt', 'a', newline='') as motorcycles:
    string_to_save = 'id\ttitle\tdate\tprice\tlocation\tlink\n'
    motorcycles.write(string_to_save)
    motorcycles.close()
  
  
  for row in li:
    with open('data/motorcycles.txt', 'a', newline='') as motorcycles:
      result_info = row.find('div', class_='result-info')
      date = result_info.find('time').text
      heading = result_info.find('h3', class_='result-heading')
      title = heading.a.text
      link = heading.a.attrs['href']
      id = heading.a.attrs['id']
      meta = result_info.find('span', class_='result-meta')
      price = meta.find('span', class_='result-price').text
      location = meta.find('span', class_='result-hood').text
      
      string_to_save = f'{id}\t{title}\t{date}\t{price}\t{location}\t{link}\n'
      motorcycles.write(string_to_save)
      motorcycles.close()
      print('Result saved.')