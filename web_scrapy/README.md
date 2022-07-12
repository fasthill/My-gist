###  Error Message: element not interactable error 발생 처리
        # driver.find_element(By.ID, 'widgetFieldDateRange').send_keys(Keys.ENTER)
        # Message: element not interactable error발생시 아래처럼 강제로 javascript로 click해주어야 함.
        element = driver.find_element(By.ID, 'widgetFieldDateRange')  
        driver.execute_script("arguments[0].click();", element)

### [Codetorial-BeautifulSoup](https://codetorial.net/beautifulsoup/index.html)
