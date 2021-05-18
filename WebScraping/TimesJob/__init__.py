import requests
from bs4 import BeautifulSoup
pages =[]
pages.append('https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating')
x=8
for i in range(x):
    pages.append('https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start={}01&ref_=adv_nxt'.format(i+2))


for i in pages:
    html_text = requests.get(i).text
    soup = BeautifulSoup(html_text, 'html.parser')
    movies = soup.find_all('div', class_='lister-item mode-advanced')
    for movie in movies:
        movieName = movies.find('a', href_='/title/tt0111161/?ref_=adv_li_tt')
        print(movieName)