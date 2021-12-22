import requests
from dotenv import dotenv_values
import json

config = dotenv_values('.env')

base_url = 'https://api.gateway.attomdata.com/propertyapi/v1.0.0/'


headers = {
  'APIkey': config['ATTOM_API_KEY'],
  'accept': 'application/json',
  'Accept': 'application/json',
}

def get_sales_by_zip(zip_code):
  url = f'https://api.gateway.attomdata.com/propertyapi/v1.0.0/salestrend/snapshot?geoid=ZI{zip_code}&interval=monthly&startyear=2015&endyear=2017&startmonth=January&endmonth=December'
  print(url)
  r = requests.get(url, headers=headers)
  print('ATTOM API request status ' + str(r.status_code))
  return r.text

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