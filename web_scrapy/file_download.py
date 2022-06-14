import wget
url="https://raw.githubusercontent.com/fasthill/My-gist/main/data/Automobile_data.csv"
response = wget.download(url, 'file_name.csv')

import requests
url="https://raw.githubusercontent.com/fasthill/My-gist/main/data/Automobile_data.csv"
response = requests.get(url)
open("file_name.csv", "wb").write(response.content)

from urllib import request
url="https://raw.githubusercontent.com/fasthill/My-gist/main/data/Automobile_data.csv"
response = request.urlretrieve(url, "file_name.csv")

import pandas as pd
url="https://raw.githubusercontent.com/fasthill/My-gist/main/data/Automobile_data.csv"
df = pd.read_csv(url)
df.head()
