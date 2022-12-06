import requests
from pprint import pprint


API_Key = '3f1a5fd9ef654a5099fa6ea0da519752'
place = input('Enter a place:\t')
url = "https://openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q" + place

weather = requests.get(url).json()

pprint(weather)