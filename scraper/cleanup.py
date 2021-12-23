def cleanup_data():
  with open('data/motorcycles.txt', 'r+') as motorcycles:
    motorcycles.truncate(0)
    motorcycles.close()
    
cleanup_data()
