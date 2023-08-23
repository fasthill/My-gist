driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

# or

from selenium.webdriver import ActionChains # scroll down 사용하기 위하여 선서

# id가 jsOpenView_1 인 element 를 찾음
stop_tag = driver.find_element(By.ID, 'jsOpenView_1')

# jsOpenView_1 element 까지 스크롤
action = ActionChains(driver)
action.move_to_element(stop_tag).perform()
