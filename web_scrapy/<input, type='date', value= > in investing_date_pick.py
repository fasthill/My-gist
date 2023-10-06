import pandas as pd
import numpy as np

from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup as bs

import requests
import datetime
import time
from datetime import date
import os, sys

import chromedriver_autoinstaller

driver_name = chromedriver_autoinstaller.install() 
time.sleep(1)

driver = wd.Chrome(service=Service(ChromeDriverManager().install()))

def get_date(start_date, end_date):
    driver.find_element(By.CLASS_NAME, 'DatePickerWrapper_icon__Qw9f8').click()

    start = driver.find_elements(By.CLASS_NAME, 'NativeDateInput_root__wbgyP')[0]
    end = driver.find_elements(By.CLASS_NAME, 'NativeDateInput_root__wbgyP')[1]

    start_element = start.find_element(By.CSS_SELECTOR, 'input[type=date]')
    end_element = end.find_element(By.CSS_SELECTOR, 'input[type=date]')

    end_date1 = "2023-19-281" # 마지막 값을 추가해서 value 값을 ''으로 바꿈. 왜 그런지는 모르겠음.
    end_element.send_keys(end_date1) # 맨처음 value값을 ''으로 바꿈
    time.sleep(0.5)

    start_element.send_keys(start_date) # 두번째로 시작일자 입력
    start_element.click()
    time.sleep(0.5)

    end_element.send_keys(end_date)  # 세번째 마지막으로 마감일자 입력 
    end_element.click()
    time.sleep(0.5)

    driver.find_element(By.CLASS_NAME, 'inv-button.HistoryDatePicker_apply-button__fPr_G').click()
    
    return

main_url = 'https://www.investing.com/indices/us-30-historical-data'
driver.get(main_url)
time.sleep(1)

today = datetime.datetime.today().date()
today_str = today.strftime('%Y-%m-%d')

start_date = '2021-12-20'

get_date(start_date, today_str)

table_class = 'datatable_table__D_jso datatable_table--border__B_zW0 datatable_table--mobile-basic__W2ilt datatable_table--freeze-column__7YoIE'
df = pd.read_html(driver.page_source, attrs={"class": table_class}, flavor=["lxml", "bs4"])[0]

df.head()

driver.close()
driver.quit()

