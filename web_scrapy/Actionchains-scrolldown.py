from selenium.webdriver import ActionChains # scroll down 사용하기 위하여 선서

# Message: element not interactable Error 방지용. 클릭하기 위하여는 그 위치가 클릭할 수 있게 노출되어 있어야 함
# 투자자별 거래실적 버튼이 위치한 곳으로 화면 scroll 

# id가 jsOpenView_1 인 element 를 찾음
stop_tag = driver.find_element(By.ID, 'jsOpenView_1')

# jsOpenView_1 element 까지 스크롤
action = ActionChains(driver)
action.move_to_element(stop_tag).perform()
