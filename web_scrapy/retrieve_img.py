import urllib.request

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) \
           AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

opener = urllib.request.build_opener()
opener.addheaders = [items for items in headers.items()]
urllib.request.install_opener(opener)
url = 'https://cdn.pixabay.com/photo/2017/02/20/18/03/cat-2083492_640.jpg'
urllib.request.urlretrieve( url, "picname.jpg")
