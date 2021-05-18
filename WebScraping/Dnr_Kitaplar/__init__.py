import requests
from bs4 import BeautifulSoup

bookNumber = 0
x = int(input())
pages = []

i=2
while x!= i:
    html_text = requests.get('https://www.dr.com.tr/kategori/Kitap/Edebiyat/grupno=00055#/page='+str(i+2)+'/sort=soldcount,desc/categoryid=0,10001,10070/parentId=10070/lg=/price=undefined')
    soup = BeautifulSoup(html_text.text, 'lxml')
    books = soup.find_all('div', class_='cell')
    for book in books:
        author = book.find('a', class_='who')
        bookName = book.find('h3', class_='ellipsis')
        print('Author Name: ' + author.text)
        print('Book Name: ' + bookName.text)
        print('------------------------------------------')
    print("*************************************************")
    i+=1
