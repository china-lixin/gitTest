#! python3
# lucky.py - Opens several Google search results.
import bs4
import requests
import sys
import webbrowse

print('Baidu is doing...')  # display text while downloading the Google page
res = requests.get('http://baidu.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)
# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://baidu.com' + linkElems[i].get('href'))
