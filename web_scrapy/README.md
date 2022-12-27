###  Error Message: element not interactable error 발생 처리
        # driver.find_element(By.ID, 'widgetFieldDateRange').send_keys(Keys.ENTER)
        # Message: element not interactable error발생시 아래처럼 강제로 javascript로 click해주어야 함.
        element = driver.find_element(By.ID, 'widgetFieldDateRange')  
        driver.execute_script("arguments[0].click();", element)
        
###  Forbidden 403,  Attention Required, Cloudflare error
        # import cfscrape
        # scraper = cfscrape.create_scraper()
        # res = scraper.get(url, headers= , cookies= )
        # res.text
        # https://qna.programmers.co.kr/questions/9558/ 참조
         . cloudscraper라는 다른 모듈이 있는데 이것도 작동하는 것 같습니다. 

### Chrome Dev를 위한 마우스 오른쪽 클릭이 안될 때. -> shift +ctrl + i 동시 클릭

### [Codetorial-BeautifulSoup](https://codetorial.net/beautifulsoup/index.html)
