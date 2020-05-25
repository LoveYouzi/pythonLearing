from bs4 import BeautifulSoup

filePath = r"/home/huizi/文档/test.html"
file = open(filePath,'r')
html = file.read()
bs = BeautifulSoup(html,'html.parser')
print(bs.title)
# print(bs.prettify()) # 格式化html结构
print(bs.find_all('span'))
file.close()
