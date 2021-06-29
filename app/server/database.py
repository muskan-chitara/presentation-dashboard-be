import motor.motor_asyncio
from bson.objectid import ObjectId
from pymongo import MongoClient

MONGO_DETAILS = "mongodb://localhost:27017"

client = MongoClient()

database = client.events

event_collection = database.get_collection("event_collection")

# helpers
def event_helper(event) -> dict:
    return {
        "id": str(event["_id"]),
        "date": event["date"],
        "duration": event["duration"],
        "title": event["title"],
        "link": event["link"],
        "summary": event["summary"],
        "attachment": event["attachment"],
    }



from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://investor.weyerhaeuser.com/events-and-presentations'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.implicitly_wait(10)

def extractClass(markup, tag_name, class_name, output_type):
    data = markup.find(tag_name, {'class': class_name})
    
    if not data:
        return 'NA'

    if output_type == 'text':
        return data.get_text()
    else:
        find_all_a = data.find_all("a", href=True)
        return find_all_a[0].get('href', '') if isinstance(find_all_a, list) else ''

def extractPptData(markup):
    date = extractClass(markup, 'div', 'item_date wd_event_sidebar_item wd_event_date', 'text')
    duration = extractClass(markup, 'div', 'item_time wd_event_sidebar_item wd_event_time', 'text')
    title = extractClass(markup, 'div', 'wd_title', 'text')
    link = extractClass(markup, 'div', 'wd_title', 'href')
    summary = extractClass(markup, 'div', 'wd_summary', 'text')
    attachment = extractClass(markup, 'div', 'wd_attachment_title', 'href')

    ppt_data = { "date": date[1:],
                    "duration" : duration[1:] if duration != 'NA' else duration,
                    "title": title,
                    "link": link,
                    "summary": summary,
                    "attachment": attachment
    }

    return ppt_data

def extractMonthlyData(markup):
    # pass the string to a BeatifulSoup object
    soup = BeautifulSoup(markup, 'lxml')
    
    # extract presentations in given month
    item_list = soup.find_all('div', {'class': 'item'})
    monthly_data = []

    for item in item_list:
        monthly_data.append(extractPptData(item))
    
    return monthly_data

def clickOn(xpath):
    driver.find_element(By.XPATH, xpath).click()
    return

def extractUsingCSS(attr, css):
    extracted_list = [i.get_attribute(attr) for i in driver.find_elements(By.CSS_SELECTOR, css)]
    return extracted_list

# go to past events
past_events = '//span[contains(@class, "wd_events_tab_label wd_events_tab_past")]'
clickOn(past_events)

#load complete page
load_more = '//*[@id="wd_printable_content"]/div/button'
while (True):
    load_button = driver.find_element(By.XPATH, load_more)
    status = load_button.get_attribute('style')
    if status == 'display: none;':
        break
    clickOn(load_more)

# extract data month-wise
events_month = [i.get_attribute('innerHTML') for i in driver.find_elements(By.CSS_SELECTOR, ".wd_events_month")]

info = []

for month in events_month:
    monthly_data = extractMonthlyData(month)
    for i in monthly_data:
        info.append(i)
        
for i in info:
    event_collection.insert_one(i)
# print(info[0])
# print(info)

driver.quit()


# Add a new event into to the database
#def add_event(event_data: dict) -> dict:
    #event = event_collection.insert_one(event_data)
    #new_event = event_collection.find_one({"_id": event.inserted_id})
    #return event_helper(new_event)


# Retrieve all events present in the database
def retrieve_events():
    events = []
    for event in event_collection.find():
        events.append(event_helper(event))
    return events


# Retrieve a event with a matching ID
def retrieve_event(id: str) -> dict:
    event = event_collection.find_one({"_id": ObjectId(id)})
    if event:
        return event_helper(event)


# Update a student with a matching ID
# async def update_student(id: str, data: dict):
    # Return false if an empty request body is sent.
    #if len(data) < 1:
     #   return False
    #student = await student_collection.find_one({"_id": ObjectId(id)})
   # if student:
    #    updated_student = await student_collection.update_one(
   #         {"_id": ObjectId(id)}, {"$set": data}
  #      )
 #       if updated_student:
#            return True
 #       return False


# Delete a student from the database
# async def delete_student(id: str):
#    student = await student_collection.find_one({"_id": ObjectId(id)})
#    if student:
#        await student_collection.delete_one({"_id": ObjectId(id)})
#        return True