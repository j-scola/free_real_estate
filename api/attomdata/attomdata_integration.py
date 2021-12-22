import requests
import os

base_url = 'https://api.gateway.attomdata.com/propertyapi/v1.0.0/'

headers = {
  'APIkey': os.environ['ATTOM_API_KEY'],
  'accept': 'application/json'
}
print(headers['APIkey'])
def get_sales_by_zip(zip_code):
  url = base_url + 'saleshistory/snapshot'
  print(url)
  params = {
    'geoid': 'ZI' + zip_code,
    'interval': 'monthly',
    'startyear': '2017',
    'endyear': '2021',
    'startmonth': 'January',
    'endmonth': 'December',
  }
  # r = requests.get(url, headers=headers, params=params)
  r = {'data': 'test'}
  
  return r

def get_sales_by_address(data):
  url = base_url + 'sale/snapshot'

  params = {
    'geoid': 'ZI' + data['zip_code'],
    'interval': 'monthly',
    'startyear': '2017',
    'endyear': '2021',
    'startmonth': 'January',
    'endmonth': 'December',
  }
  r = requests.get(url, headers=headers, params=params)
  return r