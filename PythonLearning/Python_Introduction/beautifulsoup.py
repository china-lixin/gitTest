import numpy
import scipy
import matplotlib
import pandas
import keras
import gensim
import bs4
import requests
res = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.78716000000003&lon=-122.39544999999998#.W2EEirgam00')
res.raise_for_status()
exampleSoup = bs4.BeautifulSoup(res.text)
pElems = exampleSoup.select('p')
print(str(pElems[0]))
print('Display the other elements')
print(pElems[1])
print(len(pElems))