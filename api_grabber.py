import os.path
import csv 
import time 
import requests
import bs4

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

src_request = input('Masukkan Request : ')

url = 'https://www.hostinger.co.id/api/domain-search'

r = requests.post(url, json={"domain": src_request })
print(r.status_code)

soup = bs4.BeautifulSoup(r.text, "html.parser")

print(soup)