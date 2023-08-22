# !pip install -U selenium
# !pip install chromedriver_autoinstaller

'''
# Chrome browser version이 바뀔 때마다,
# 여기를 살피고, https://chromedriver.chromium.org/downloads/version-selection
# 여기에서, https://googlechromelabs.github.io/chrome-for-testing/
# Chrome Browser version과 맞는 chromedriver를 download 받아서 Service에 경로를 지정하여 사용하면 됨.
'''

from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import chromedriver_autoinstaller

chrome_version = chromedriver_autoinstaller.get_chrome_version() # 현재 chrome version 확인

driver_name = chromedriver_autoinstaller.install()  # chromedriver path 확인
                                      # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path
time.sleep(1)

# driver = wd.Chrome(driver_name)
service = Service(ChromeDriverManager(version="114.0.5735.90").install()) # 특정 version 지정시
options = wd.ChromeOptions()
driver = wd.Chrome(service=service, options=options)

# 혹은,
# 최근 chromedriver를 다운받아 경로 설정후 실행. 아래는 116 폴더에 chromedriver를 설치하고 실행한 예
service = Service(r"116/chromedriver.exe")  # 이제는 service를 반드시 사용해야 함.
options = wd.ChromeOptions()
driver = wd.Chrome(service=service, options=options)

# or,

chromedriver_path=r'C:/Users/user/.wdm/drivers/chromedriver/win32/116/chromedriver.exe'  # 폴더명 입력후 실행
service = Service(executable_path = chromedriver_path )
options = wd.ChromeOptions()
driver = wd.Chrome(service=service, options=options)

# Chrome browser version이 바뀔 때마다,
# 여기를 살피고, https://chromedriver.chromium.org/downloads/version-selection
# 여기에서, https://googlechromelabs.github.io/chrome-for-testing/
# Chrome Browser version과 맞는 chromedriver를 download 받아서 Service에 경로를 지정하여 사용하면 됨.
