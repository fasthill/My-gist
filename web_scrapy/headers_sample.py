import requests
from bs4 import BeautifulSoup as bs

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) \
           AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

url = 'https://kr.investing.com/commodities/crude-oil-historical-data'

res = requests.get(url, headers=headers)

soup = bs(res.text, 'html.parser')
wti = soup.select('#results_box tr')
