# url에 한글이나 non english 표현이 있어서 에러가 날 경우 사용

import urllib

new_url = urllib.parse.quote(kor_url.encode('utf8'), '/:')

# 예:
# kor_url = 'https://www.한글주소.co.kr' or img_url = 'https://www.image.co.kr/고양이.jpg'
# new_url = urllib.parse.quote(kor_url.encode('utf8'), '/:')
#         =>> 'https://www.%ED%95%9C%EA%B8%80%EC%A3%BC%EC%86%8C.co.kr'

# new_img_url = urllib.parse.quote(img_url.encode('utf8'), '/:')
#         =>> 'https://www.image.co.kr/%EA%B3%A0%EC%96%91%EC%9D%B4.jpg'
