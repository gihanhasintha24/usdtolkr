#convert usd to lkr
import requests
from time import *

url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)
rate = response.json()['rates']['LKR']
usd = float(input('enter usd:'))
lkr = usd * rate
print(lkr)
sleep(20)