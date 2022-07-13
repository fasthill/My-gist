###  Error Message: element not interactable error 발생 처리
        # driver.find_element(By.ID, 'widgetFieldDateRange').send_keys(Keys.ENTER)
        # Message: element not interactable error발생시 아래처럼 강제로 javascript로 click해주어야 함.
        element = driver.find_element(By.ID, 'widgetFieldDateRange')  
        driver.execute_script("arguments[0].click();", element)

### 마우스 오른쪽 클릭이 안될 때. -> shift +ctrl + i 동시 클릭

### [Codetorial-BeautifulSoup](https://codetorial.net/beautifulsoup/index.html)
