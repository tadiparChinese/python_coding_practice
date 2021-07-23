#fetching data from the web

import requests

url = 'http://example.com/movies.json'
r = requests.get(url)

print(r.status_code)
print(r.content)