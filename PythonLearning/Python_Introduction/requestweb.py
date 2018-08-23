import requests

res = requests.get('http://www.avic-intl.cn')
res.raise_for_status()
playFile = open('RomeoAndJuliet.html', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
