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

# extract data
ppt_dates = ["" or i.get_attribute('innerText')[1:] for i in driver.find_elements(By.CSS_SELECTOR, ".item_date")]
ppt_times = ["" or i.get_attribute('innerText')[1:] for i in driver.find_elements(By.CSS_SELECTOR, ".item_time")]
ppt_titles = [i.get_attribute('innerText') for i in driver.find_elements(By.CSS_SELECTOR, ".wd_title")]
summary = [i.get_attribute('innerText') for i in driver.find_elements(By.CSS_SELECTOR, ".wd_summary")]

attachment = [i.get_attribute('href') for i in driver.find_elements(By.CSS_SELECTOR, ".wd_attachment_title a")]
print(attachment)

driver.quit()

data = []
for i in zip(ppt_dates, ppt_times, ppt_titles, summary, attachment):
    data.append(i)

df_bs = pd.DataFrame(data, columns=['Date', 'Time (if available)', 'Presentation title', 'Presentation summary (if available)', 'Attachment (if any)'])
