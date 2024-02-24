from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import requests
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd

url = "https://www.linkedin.com/jobs/search/"

def initialize_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path='./chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    return driver

driver =  initialize_driver()

driver.get(url)

cnt = 5
while(cnt > 0):
    try:
        more_btn = jobs_div = WebDriverWait(driver,0.5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'button[aria-label="See more jobs"]'))
        )
        more_btn.click()
        cnt -= 1
    except:
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        

jobs_div = WebDriverWait(driver,5).until(
    EC.element_to_be_clickable((By.CLASS_NAME,"jobs-search__results-list"))
)

jobs = jobs_div.find_elements(By.CSS_SELECTOR,"a[data-tracking-control-name='public_jobs_jserp-result_search-card']")

def get_job_data(job_link):
    try:
        r = requests.get(job_link)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        job_title = soup.find('h1', {'class': 'topcard__title'}).text.strip()
        company_element = soup.find('a', {'class':'topcard__org-name-link'})
        company_name = company_element.text.strip()
        company_linkedin_url  = company_element.get('href').strip()
        company_location = soup.find('span',{'class':'topcard__flavor topcard__flavor--bullet'}).text.strip()
        job_posted = soup.find('span',{'class':'posted-time-ago__text'}).text.strip()
        today = str(date.today())
        
        job_data = {
            'job_title': job_title,
            'company_name': company_name,
            'company_location': company_location,
            'job_posted': job_posted,
            'scrape_date': today,
            'job_url': job_link,
            'company_linkedin_url': company_linkedin_url,
        }
        return job_data
    except Exception as e:
        print(f"{e} \n issued joblink{job_link}")
        return {}

job_links = []
for job in jobs:
    link = job.get_attribute('href')
    job_links.append(link)

job_data = []
for link in job_links:
    data = get_job_data(link)
    job_data.append(data)

df = pd.DataFrame.from_dict(job_data)
df = df.dropna()
df.to_csv("Linkedin_Jobs.csv", index=False)


