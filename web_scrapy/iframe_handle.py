
# 프레임 살펴보기
iframes = driver.find_elements(By.CSS_SELECTOR,"iframe")

for iframe in iframes:
    print("name= ", iframe.get_attribute('name'))
    print("id=", iframe.get_attribute('id'))
    print("class= ", iframe.get_attribute('class'))

WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe#iframe"))) # wait and switch to id="iframe"
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Shop Now"))).click()

driver.switch_to.default_content()  # 처음으로 빠져 나오기

# driver.back()  # 바로 전 driver로 나오기
# driver.forward() # 다음 driver로 스위치

# 프레임 전환하기

driver.switch_to.default_content()
driver.switch_to.frame('id' or 'name') 

# id나 name이 없으면 아래와 같이 먼저 element를 선택하고 switch를 하면 됨.
iframe_demo = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")  # use "Copy Xpath" in inspection.
# many examples in https://selenium-python.readthedocs.io/locating-elements.html for several different cases
# with class =, id = , name =, (By.XPATH, "//iframe[@name='XXXX'][@type='XXXX']")
driver.switch_to.frame(iframe_demo);
