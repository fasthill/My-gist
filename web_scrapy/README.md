###  CSS_SELECTOR ATTR 형식
        # driver.find_elements(By.CSS_SELECTOR, 'input[type="date"][value="2023-08-14"]') 
        # 'tagname[attr1='aaaa'][attr2='bbbb']' 형식으로 기입

###  Error Message: element not interactable error 발생 처리
        # driver.find_element(By.ID, 'widgetFieldDateRange').send_keys(Keys.ENTER)
        # Message: element not interactable error발생시 아래처럼 강제로 javascript로 click해주어야 함.
        element = driver.find_element(By.ID, 'widgetFieldDateRange')  
        driver.execute_script("arguments[0].click();", element)
        
        혹은, form 구성하여 여러개의 id가 존재할 수 있으니, 이럴 경우 아래와 같이 하면 됨. web_scrapy 폴더에 multiple_ID 항목으로 설명되어 있음.
        driver.find_element(By.XPATH, '(.//*[@id="widgetFieldDateRange"])[2]').click()
        
###  Forbidden 403,  Attention Required, Cloudflare error
        # import cfscrape
        # scraper = cfscrape.create_scraper()
        # res = scraper.get(url, headers= , cookies= )
        # res.text
        # https://qna.programmers.co.kr/questions/9558/ 참조
         . cloudscraper라는 다른 모듈이 있는데 이것도 작동하는 것 같습니다.    
         
###  json 처리
        # driver.get(url)
        # element = driver.find_element(By.CSS_SELECTOR, '...')
        # data = json.loads(element.text)
        # -----------
        # res = requests.get(url)
        # data = json.loads(res.text)
        # api 사용할 때 json 에러 -- JSONDecodeError: Expecting value: line 1 column 1 (char 0) -- 가
        # 발생할 시는 selenium을 이용하면 해결됨.

### Chrome Dev를 위한 마우스 오른쪽 클릭이 안될 때. -> shift +ctrl + i 동시 클릭

### [Codetorial-BeautifulSoup](https://codetorial.net/beautifulsoup/index.html)  

### [BeautifulSoup4.0.0문서](https://www.crummy.com/software/BeautifulSoup/bs4/doc.ko/)
