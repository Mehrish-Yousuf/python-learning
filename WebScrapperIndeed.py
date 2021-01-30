import requests as rq
from bs4 import BeautifulSoup

url = "https://pk.indeed.com/jobs?q=software+engineer&l=Karachi"
page = rq.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find( id='resultsCol')


jobListings = results.find_all('div', class_='jobsearch-SerpJobCard')

# print(jobListings)

for job in jobListings:
    # print("-------",job)

    jobTitleMain = job.find('h2', class_='title')

    title = jobTitleMain.find('a')
    company = job.find('span', class_="company")
    location = job.find('span', class_='location')
    datePosted = job.find('span', class_='date')

    print("Job title: ", title.text)
    print("Company: ", company.text)
    print('Location:', location.text)
    print('Posted: ', datePosted.text)


    summary = job.find_all('li')

    print("Summary: ", end="")
    
    for point in summary:
        print(point.text)
    


    
    



   
    



