from bs4 import BeautifulSoup
import requests
import re

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

soup = BeautifulSoup(html_text, "lxml")
#jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx').text
for jobs in soup.find_all('li', class_='clearfix job-bx wht-shd-bx'):
    # jobs_result = str(jobs.text.encode("utf-8"))
    jobs_result = jobs.text
    print(' '.join(re.findall('\w+ ', jobs_result)))
    # print(jobs_result)