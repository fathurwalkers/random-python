import os.path
import csv 
import time 
import requests
import bs4

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

# src_prefix = input("Masukkan Prefix : ")

src_request = input('Masukkan Request : ')

# user_request = str(src_request)

# prefix_request = "intext:'" + src_prefix + "'"

# prefix_index = "intext:'" + src_request + "'"

# data = {domain: '{}'.format(user_request)}

url = 'https://www.hostinger.co.id/api/domain-search'

r = requests.post(url, json={"domain": src_request })
print(r.status_code)

soup = bs4.BeautifulSoup(r.text, "html.parser")

print(soup)

# url = 'https://www.google.com/search?q={}&rlz=1C1GCEA_enID939ID939&oq={}&aqs=chrome..69i57j69i64.15590j0j4&sourceid=chrome&ie=UTF-8'.format(prefix_request, prefix_index)

# try:
#     response = requests.post](url)
#     soup = bs4.BeautifulSoup(response.text, "html.parser")
#     print(soup)
# except requests.exceptions.RequestException as e:
#     print(e)
#     exit()

