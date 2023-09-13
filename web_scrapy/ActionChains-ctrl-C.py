from selenium.webdriver import ActionChains # 
from selenium.webdriver.common.keys import Keys

url = 'https://www.coupang.com/'
driver = webdriver.Chrome()
# 웹사이트 이동
driver.get(url)

# ctrl키를 놓지 않고 누르고, 'c' 키를 보낸 뒤 ctrl키를 놓은 것을 실행
ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

# 원하는 요소(element)를 찾습니다. 이 경우에는 검색창입니다.
element = driver.find_element(By.ID, 'headerSearchKeyword')
# 다음과 같은 동작을 하는 액션 체인을 만들었습니다.
# 검색창을 찾고 '아이스크림'이라는 검색어를 입력한 뒤 Enter를 입력합니다.
actions = ActionChains(driver).send_keys_to_element(element, '아이스크림').send_keys(Keys.ENTER)
# 체인을 실행합니다.
actions.perform()

ActionChains(driver).move_to_element(element) # element로 마우스 이동
ActionChains(driver).click(element)  # element 마우스 클릭	
ActionChains(driver).send_keys_to_element(element, 'name') # element 키보드 'name' 입력
ActionChains(driver).send_keys('name') # 키보드 입력	
