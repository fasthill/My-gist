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

element = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '---'))  # 해당 요소가 페이지에 존재하며 화면에 표시되어 있는지 확인
    )

element = WebDriverWait(driver, 5).until(
        EC.visibility_of(driver.find_element(By.XPATH, '----'))
    )

# https://mebadong.tistory.com/101 를 기반으로 작성
