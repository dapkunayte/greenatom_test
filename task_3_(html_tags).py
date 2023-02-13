from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

req = Request('https://greenatom.ru', headers={'User-Agent': 'Mozilla/5.0'})
data = urlopen(req)
soup = BeautifulSoup(data, 'html.parser')

# сумма по массиву, который содержит количество атрибутов для каждого тега
attr_count = sum([len(ele.attrs) for ele in soup.find_all()])

# длина массива, в котором содержатся имена всех тегов
tags_count = len([ele.name for ele in soup.find_all()])

print(tags_count, attr_count)