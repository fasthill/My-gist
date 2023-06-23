from bs4 import BeautifulSoup as bs
import requests

import pandas as pd

import cfscrape
scraper = cfscrape.create_scraper()

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) \
           AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

url = 'https://www.investing.com/indices/nq-100-futures-historical-data'

r = scraper.get(url, headers=headers)
html = r.content

class_name = "datatable_table__D_jso datatable_table--border__B_zW0 datatable_table--mobile-basic__W2ilt datatable_table--freeze-column__7YoIE"

table = pd.read_html(html, attrs={"class": class_name},flavor=["lxml", "bs4"])[0]

table.head()

soup = bs(html, 'html.parser')
print(soup.prettify())
