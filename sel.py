from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

url = 'https://investor.weyerhaeuser.com/events-and-presentations'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.implicitly_wait(10)

# go to past events
driver.find_element(By.XPATH, "//span[contains(@class, 'wd_events_tab_label wd_events_tab_past')]").click()

# extract list of months
ppt_dates = [i.text for i in driver.find_elements(By.XPATH, "//div[contains(@class, 'item_date wd_event_sidebar_item wd_event_date')]")]
ppt_times = [i.text for i in driver.find_elements(By.XPATH, "//div[contains(@class, 'item_time wd_event_sidebar_item wd_event_time')]")]
ppt_titles = [i.text for i in driver.find_elements(By.XPATH, "wd_title")]
# pdf_links = [i.text for i in driver.find_elements(By.XPATH, "//div[contains(@class, 'wd_events_month_header')]")]
ppt_summary = [i.text for i in driver.find_elements(By.XPATH, "//div[contains(@class, 'wd_summary')]")]
pdf_titles = [i.text for i in driver.find_elements(By.XPATH, "//div[contains(@class, 'wd_attachment_title')]")]
# pdf_links = [i.text for i in driver.find_elements(By.XPATH, "//div[contains(@class, 'wd_events_month_header')]")]

# print('title is: ', driver.find_element(By.XPATH, "//div[contains(@class, 'item_time wd_event_sidebar_item wd_event_time')]"))

print('length of ppt_dates: ', len(ppt_dates))
for i in ppt_titles:
    print('ppt_date is: ', i)

# data = []
# for i in zip(ppt_dates, ppt_times, ppt_titles, ppt_summary, pdf_titles):
#     data.append(i)

# df_bs = pd.DataFrame(data, columns=['Date', 'Time', 'Presentation title', 'Presentation summary', 'Attachment (if any)'])
# df_bs.to_csv('InvestorsPpt.csv')