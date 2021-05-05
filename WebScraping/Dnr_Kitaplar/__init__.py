import requests
from bs4 import BeautifulSoup

bookNumber = 0
x = int(input())
pages = []
for i in range(x):
    pages.append(
        f'https://www.dr.com.tr/kategori/Kitap/Edebiyat/grupno=00055#/page={i}/sort=soldcount,desc/categoryid=0,10001,10070/parentId=10070/lg=/price=undefined')

for page in range(len(pages)):
    print(pages[page])
    html_text = requests.get(pages[page]).text
    soup = BeautifulSoup(html_text, 'lxml')
    books = soup.find_all('div', class_='cell')

    author = book.find('a', class_='who').text
    bookName = book.find('h3', class_='ellipsis').text
    print('Author Name: ' + author)
    print('Book Name: ' + bookName)
    bookNumber += 1
    print('------------------------------------------')


