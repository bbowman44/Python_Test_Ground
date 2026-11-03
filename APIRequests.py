import requests

# documentation for using the requests library: https://requests.readthedocs.io/en/latest/user/quickstart/
# potential api that I can call to try out: https://finnhub.io/

url = 'https://api.github.com/events'

r = requests.get(url)

#print(r.url)
#print(r.status_code)
#print(r.text)
#print(r.encoding)
#print(r.content)
#print(r.json())
#print(r.headers)