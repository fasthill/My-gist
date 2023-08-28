from urllib.request import urlretrieve
import zipfile

urlretrieve("http://files.grouplens.org/datasets/movielens/ml-100k.zip", "movielens.zip")  # 'movielens.zip'로 저장
zip_ref = zipfile.ZipFile('movielens.zip', 'r') # 'movielens.zip'을 instance
zip_ref.extractall() # 'movielens.zip'을 현재 폴더에 unzip

print(zip_ref.read('ml-100k/u.info')) # unzip된 폴더에서 파일을 읽어서 내용을 프린트


from urllib.request import urlretrieve
import tarfile

urlretrieve("https://raw.githubusercontent.com/rickiepark/handson-ml2/master/datasets/housing/housing.tgz", "housing.tgz")
housing_tgz = tarfile.open("housing.tgz")
# housing_tgz.extractall(path=housing_path)  # 정해진 folder에 저장
housing_tgz.extractall()  # 현재 폴더에 저장
housing_tgz.close()
