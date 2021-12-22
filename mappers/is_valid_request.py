import re

def is_valid_request(request_data):
  
  # this should read the keys on request data, 
  # check each one individually
  # and return true if all are valid
  
  valid_request = True
  
  if 'zip_code' in request_data:
    zip_code = str(request_data['zip_code'])
    regex = re.compile('^[0-9][0-9][0-9][0-9][0-9]$', re.I)
    print('zip code ' + zip_code)
    match = regex.match(zip_code)
    print('valid zip = ' + str(bool(match)))
    if not bool(match):
      return False
  
  
  return valid_request
    