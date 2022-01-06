#Indeed Job Scraper

#Package
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd

#Create Headers
position = '"Data Analyst"'
location = 'Indonesia'
url = 'https://id.indeed.com/jobs?q={}&l={}&start='.format(position, location)
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
    }

#Inisiasi List datas
datas = []

#Looping page
count_page = 0
for page in range(0, 1850, 10):
    
    count_page+=10
    print('scraping page :', count_page)

    response = requests.get(url+str(page), headers=headers) #print(response) result : response 200 'OK'
    soup = BeautifulSoup(response.text, 'html.parser')
    boxs = soup.find_all('div', 'job_seen_beacon')
    for box in boxs:
        job_title = box.find('div', class_="heading4 color-text-primary singleLineTitle tapItem-gutter").text.replace('Baru', '').strip()
        company_name = box.find('span', class_="companyName").text.strip()
        location = box.find('div', class_="companyLocation").text.replace('•', ' / ').strip()
        try : salary_month_Rp = box.find('div', class_="heading6 tapItem-gutter metadataContainer").text.replace(' per bulan', '').replace('Rp. ', '').strip()
        except : salary_month_Rp = ''
        posted_days_ago = box.find('span', class_="date").text.replace('Posted', '').replace(' hari yang lalu', '').replace('EmployerAktif ', '').strip()
        today = datetime.today().strftime('%Y-%m-%d')
        summary = box.find('div', class_="job-snippet").text.strip().replace('\n', ' ').replace('…', '').strip()
    
        job = {
            'job_title': job_title,
            'company_name': company_name,
            'location': location,
            'salary_month_Rp': salary_month_Rp,
            'posted_days_ago': posted_days_ago,
            'today': today,
            'summary': summary
        }
        datas.append(job)

#save to csv
df = pd.DataFrame(datas)
print(df.head())
df.to_csv('indeed14.csv')