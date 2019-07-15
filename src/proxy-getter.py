# import dependencies
from bs4 import BeautifulSoup
import requests

url = 'https://free-proxy-list.net/' # https://www.us-proxy.org/ works too
proxies = []

request = requests.get(url) # send a request to the url, so we can get it's content
soup = BeautifulSoup(request.text, 'html.parser') # create a soup for it, so we can parse it

# messy code starts
for tbody in soup.find_all('tbody'):
    for tr in tbody.find_all('tr'):
        for td in tr.find_all('td'):
            if '.' in td.text: # check if it's an ip if there's a . in them, there are other tds such as how long ago it was added
                proxies.append(td.text) # append it to the proxies list so we can save it

# pretty much save the proxies
file = open('./proxies.txt', 'w') 
for proxy in proxies:
    file.write(proxy + '\n')
file.close()