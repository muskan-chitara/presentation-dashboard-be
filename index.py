import requests
from bs4 import BeautifulSoup
import pandas as pd

# url to scrape data from
url = 'https://investor.weyerhaeuser.com/events-and-presentations'

# make a request to the site and get it as a string
markup = requests.get(url).text

# pass the string to a BeatifulSoup object
soup = BeautifulSoup(markup, 'html.parser')

# extract title
title = soup.select('title')
site_name = title[0].text
print('Scraping from: ', site_name)

# extract ppt date and time
ppt_date = soup.find_all('div', {'class': 'item_date wd_event_sidebar_item wd_event_date'})
dates = [i.text for i in ppt_date]

# for date_time in ppt_date:
#     print(date_time.get_text())

# extract ppt names and links
ppt_title = soup.find_all('div', {'class': 'wd_title'})
print('Total number of ppts: ', len(ppt_title))

ppts = list()
links = list()

for item in ppt_title:
    title = item.text
    title_link = item.findChildren("a" , recursive=False)[0]
    ppts.append(title)
    links.append(title_link.attrs['href'])
    # print('link: ', title_link.attrs['href'])

data = []

for i in zip(dates, ppts, links):
    data.append(i)

df_bs = pd.DataFrame(data, columns=['Date_time', 'Presentation', 'Presentation link'])
df_bs.set_index('Date_time',inplace=True)
df_bs.to_csv('InvestorsPpt.csv')
