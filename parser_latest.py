from bs4 import BeautifulSoup
import requests
import re

# Counter of pages on site and movies in list:
def pages_and_movies_counter():
    cntPage = 1 # page counter (1 to inf)
    cntMovie = 0 # movie counter (0 to 4, only 5 movies on a page)
    while True:
        yield cntPage, cntMovie # generator object (page, movie)
        cntMovie += 1
        if cntMovie > 4: # then movie counter exceeds 5:..
            cntPage += 1 # ..page counter turns page..
            cntMovie = 0 # ..and resets movie counter

counter = pages_and_movies_counter() # class generator
counterTuple = next(counter) # class tuple
pageNumber = counterTuple[0] # class int
movieNumber = counterTuple[1] # class int

# Constructing source url for soup and scraping:
def source_constructor(page_number):
    base = "https://whereyouwatch.com/latest-reports/?pg="
    source = base + str(page_number)
    return source

<<<<<<< HEAD
url = source_constructor(pageNumber) # class str

# Source scraping by attribute <jrResourceContent> on a page:
def page_scraper(source_url):
    response = requests.get(source_url)
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    scraped_reports = soup.find_all(class_="jrResourceContent") # class set
    return scraped_reports

scrapedPage = page_scraper(url) # class bs4.element.ResultSet

# Movie parsing to a 5-item list from scraped page:
def page_parser(scraped_page):
    raw_movies_list = [] # list of movies, 5 items
    for report in scraped_page:
        raw_movie_data = [] # single movie as a list of variables, 7 items
        # Variables parsing from scraped page:
        report_name = report.find(class_="jrResourceTitle") # report name
        report_movie = report.find(class_="jrResourceListingTitle") # movie title
        report_link = report_movie.find('a', attrs={'href': re.compile("^https://")}) # link to report page
        submition_username = report.find(class_="jrResourceUserLabel") # reporter name
        submition_userlink = submition_username.find('a', attrs={'href': re.compile("^https://")}) # ink to reporter page
        submition_time = report.find(class_="jrResourceCreatedDate") # report date
        report_description = report.find(class_="jrResourceDescription") # report description
        # Variables formatting:
        raw_movie_data.append(report_name.get_text().strip('\n'))
        raw_movie_data.append(report_movie.get_text().strip('\n'))
        raw_movie_data.append(report_link.get('href'))
        raw_movie_data.append(submition_username.get_text().strip('\n'))
        raw_movie_data.append(submition_userlink.get('href'))
        raw_movie_data.append(submition_time.get_text().strip('\n'))
        if str(type(report_description)) == "<class 'NoneType'>": # if report description is absent:..
            raw_movie_data.append('No Description') # ..put empty value to keep constant length of list
        else:
            raw_movie_data.append(report_description.get_text().strip('\n'))
        raw_movies_list.append(raw_movie_data)
    return raw_movies_list

parsedPage = page_parser(scrapedPage) # class list
=======
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
>>>>>>> ca76f5002b5acb9ecca50e58c0339bcc301afba1

# Yields single formatted movie:
def present_movie(list):
    for movie in parsedPage:
        yield movie

showMovie = present_movie(parsedPage) # class generator
showNextMovie = next(showMovie) # class list
