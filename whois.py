import sys 
import os 
import requests, re, warnings, argparse
import urllib.request
from fake_useragent import UserAgent
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore', InsecureRequestWarning)
from bs4 import BeautifulSoup

ua = UserAgent()
sess = requests.Session()
src_request = input('Masukkan Request : ')
url = sess.get('https://www.hostinger.co.id/api/domain-search', headers={'User-Agent': ua.chrome}, allow_redirects=False)
payload = {"domain":src_request}
def doRequest():
    source = 'https://www.hostinger.co.id/whois'
    getPost = requests.post(source, data=payload).text
    soup = BeautifulSoup(getPost, 'html.parser')
    print(soup.prettify())
    
doRequest()





