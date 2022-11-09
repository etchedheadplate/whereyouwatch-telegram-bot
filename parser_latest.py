from bs4 import BeautifulSoup
import requests
import re

source = "https://whereyouwatch.com/latest-reports/?pg="
page = 2
url = source + str(page)

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")
latest_reports = soup.find_all(class_="jrResourceContent")

def page_counter():
    pageNum = 1
    return str(pageNum)

def return_multiple():
    return [1,2,3,4,5,6,7]


# придется чото думать с кортежами:
'''def show_latest(source, page):
    latest_movies = []

    # page_counter = 1
    # movie_counter = 0

    for report in latest_reports:
        movie = tuple()

        report_name = report.find(class_="jrResourceTitle")
        report_movie = report.find(class_="jrResourceListingTitle")
        report_link = report_movie.find('a', attrs={'href': re.compile("^https://")})
        submition_username = report.find(class_="jrResourceUserLabel")
        submition_userlink = submition_username.find('a', attrs={'href': re.compile("^https://")})
        submition_time = report.find(class_="jrResourceCreatedDate")
        report_description = report.find(class_="jrResourceDescription")
        
        movie.append(report_name.get_text().strip('\n'))
        movie.append(report_movie.get_text().strip('\n'))
        movie.append(report_link.get('href'))
        movie.append(submition_username.get_text().strip('\n'))
        movie.append(submition_userlink.get('href'))
        movie.append(submition_time.get_text().strip('\n'))
        if str(type(report_description)) == "<class 'NoneType'>":
            movie.append('No Description')
        else:
            movie.append(report_description.get_text().strip('\n'))
        
        latest_movies.append(movie)
    
    for movie in latest_movies:
        return movie

print(show_latest(url, page))'''

