import time
import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.hepsiburada.com/kampanyalar/kadin-gunluk-ayakkabi")
r.status_code
soup = BeautifulSoup(r.content,"lxml")
st2 = soup.find_all("li",class_="search-item col lg-1 md-1 sm-1  custom-hover not-fashion-flex").text
print(st2)