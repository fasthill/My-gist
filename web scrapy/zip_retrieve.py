from urllib.request import urlretrieve
import zipfile

urlretrieve("http://files.grouplens.org/datasets/movielens/ml-100k.zip", "movielens.zip")  # 'movielens.zip'로 저장
zip_ref = zipfile.ZipFile('movielens.zip', 'r') # 'movielens.zip'을 instance
zip_ref.extractall() # 'movielens.zip'을 현재 폴더에 unzip

print(zip_ref.read('ml-100k/u.info')) # unzip된 폴더에서 파일을 읽어서 내용을 프린트
