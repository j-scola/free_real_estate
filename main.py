from flask import Flask, request, render_template
from flask_cors import CORS
import requests
import json

from mappers.is_valid_request import is_valid_request
from api.attomdata.attomdata_integration import get_sales_by_zip

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['POST', 'GET'])
def index():
  if request.method == 'POST':
    zip_code = request.form['zip-input']
    if is_valid_request({'zip_code': zip_code}):
      # request zip code data from api 
      return json(get_sales_by_zip(zip_code))
    
    return 'post recieved'
  
  else: 
    return render_template('zip.html')

if __name__ == '__main__':
  app.run('0.0.0.0', 5000, debug=True)