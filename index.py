import requests
from bs4 import BeautifulSoup

# make a request to the site and get it as a string
markup = requests.get(f'https://investor.weyerhaeuser.com/events-and-presentations').text

# pass the string to a BeatifulSoup object
soup = BeautifulSoup(markup, 'lxml')
# print(type(soup))

# title = soup.select('title')
# site_name = title[0].text
# print('Scraping from: ', site_name)

#this will hold all the months
months = []
month_list = soup.select('.wd_events_month_header')
print(len(month_list))

# now we can select elements
for item in soup.select('.wd_events_month_header'):
    print(item.text)
    # month = {}
    # month['text'] = item.select_one('.text').get_text()
    # month['author'] = item.select_one('.author').get_text()

    # # get the tags element
    # tags = item.select_one('.tags')

    # # get each tag text from the tags element
    # month['tags'] = [tag.get_text() for tag in tags.select('.tag')]
    # months.append(month)
    
# print(months)
