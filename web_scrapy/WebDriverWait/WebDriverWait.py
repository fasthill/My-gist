EC.title_is(...)
EC.title_contains(...)
EC.presence_of_element_located(...)
EC.visibility_of_element_located(...)
EC.visibility_of(...)
EC.presence_of_all_elements_located(...)
EC.text_to_be_present_in_element(...)
EC.text_to_be_present_in_element_value(...)
EC.frame_to_be_available_and_switch_to_it(...)
EC.invisibility_of_element_located(...)
EC.element_to_be_clickable(...)
EC.staleness_of(...)
EC.element_to_be_selected(...)
EC.element_located_to_be_selected(...)
EC.element_selection_state_to_be(...)
EC.element_located_selection_state_to_be(...)
EC.alert_is_present(...)

driver.get("https://naver.com")

element = WebDriverWait(driver, 10).until(
    EC.title_is('NAVER')  # title_is는 head에 선언된 title의 속성을 비교
    )

element = WebDriverWait(driver, 10).until(
        EC.title_contains('VER') # title에 특정내용이 있는지 확인
    )

element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '---'))  # DOM에 요소가 있는지 확인
    )

element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '---'))  # 해당 요소가 페이지에 존재하며 화면에 표시되어 있는지 확인
    )

element = WebDriverWait(driver, 10).until(
        EC.visibility_of(driver.find_element(By.XPATH, '----'))
    )

element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '---'))
    )

wait = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, '------'), "this is text") # 지정된 element의 text의 내용이 일지하는지    
        # 예 <p>this is text</p>     
    )
    
wait = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element_value((By.XPATH, '-------'), # 지정된 element의 value와 일치 여부 확인
                                                'text value')
        # 예: <input type="text" value="text value">  # element 내 value attribute 값 일치 여부
        # <input type="button" value="button text value">
    )
  
# https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html
