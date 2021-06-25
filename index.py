import requests
from bs4 import BeautifulSoup

# make a request to the site and get it as a string
markup = requests.get(f'https://investor.weyerhaeuser.com/events-and-presentations').text

# pass the string to a BeatifulSoup object
soup = BeautifulSoup(markup, 'html.parser')
# print(type(soup))

title = soup.select('title')
site_name = title[0].text
print('Scraping from: ', site_name)

# events_list = soup.select('.wd_events_list')
# print(len(events_list))
# print(events_list)

li = soup.find_all('div', {'class': 'item_date wd_event_sidebar_item wd_event_date'})
print(len(li))

for item in li:
    print(item.get_text())

# dates = soup.find_all('div', {'class': 'wd_events_month_header'})
# print('length of year: ', len(dates))

# for item in dates:
#     print(item.get_text())

title = soup.find_all('div', {'class': 'wd_title'})
print('length of title list: ', len(title))

for item in title:
    print(item.get_text())
    title_link = item.findChildren("a" , recursive=False)[0]
    print('link: ', title_link.attrs['href'])
