import time

import requests
from bs4 import BeautifulSoup
def find_job():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for job in jobs:
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')
        skills = job.find('span', class_='srp-skills').text.replace(' ','')
        published_day = job.find('span', class_='sim-posted').text
        if('few' in published_day):
            continue
        print(f'Company Name: {company_name.strip()}')
        print(f'Required Skills: {skills.strip()}')
        print(f'Post Day: {published_day.strip()}')
        print('')

if __name__ =='__main__':
    while True:
        find_job()
        print('waiting')
        time.sleep(10)