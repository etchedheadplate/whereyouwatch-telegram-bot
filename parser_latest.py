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

def return_sublist(list): # takes list, returns each item of sublist of list as a string
    for sublist in list:
        for string in sublist:
            yield string * len(sublist)

def show_latest(source, page):
    latest_releases = [] # list of last 5 movie releases, each release is a list itself

    for report in latest_reports:
        movie = [] # last movie release as a list of 7 items (5 text and 2 URLs)

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
        
        latest_releases.append(movie)

    return latest_releases

latest_movies = show_latest(url, page)
movie_surfer = return_sublist(latest_movies)

print(next(movie_surfer))
print(next(movie_surfer))

