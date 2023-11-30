from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import datetime
import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
# conn = sqlite3.connect('Taskmaster//taskmaster.db')
# cursor = conn.cursor()
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# desired_capabilities = DesiredCapabilities.CHROME.copy()
# desired_capabilities['acceptInsecureCerts'] = True
# driver = webdriver.Chrome(desired_capabilities=desired_capabilities)
options = Options()

if __name__ == "__main__":
    driver = webdriver.Chrome(options=options)
    series_list =["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Champion_of_Champions"]
    data_file = open("Taskmaster//data.txt", "w")
    for series in series_list:
        if series != "Champion_of_Champions":
            driver.get("https://taskmaster.fandom.com/wiki/Series_"+series)
        else:
            driver.get("https://taskmaster.fandom.com/wiki/Champion_of_Champions")
        # # scroll down to the bottom of the page
        # # get the whole table of tasks for the series it has class "tmtable"
        # driver.execute_script("window.scrollBy(0,1500)","")
        # driver.implicitly_wait(10)
        # data_file.write("Hello!")
        # table = driver.find_element(By.CSS_SELECTOR, "class=tmtable")
        # # get all the rows from the table
        # rows = table.find_elements(By.TAG_NAME, "tr")
        # for row in rows:
        #     #check if the row is a header row
        #     if row.get_attribute("class") == "tmtableheader":
        #         contestants = row.find_elements(By.TAG_NAME, "a").title
        #         data_file.write(contestants)
        #         # print("contestants are:", contestants)
        #     elif row.get_attribute("class") == "tmtableepisode": 
        #         title = row.find_element(By.TAG_NAME, "a").text
        #         data_file.write(title)
        #         # print("episode title:", title)
        #     elif row.get_attribute("class") == "tmtabletotal":
        #         final_scores= row.find_elements(By.TAG_NAME, "td")
        #         highscore = row.find_element(By.CLASS_NAME, "tmtablewinner").text
        #         winner_id = final_scores.indexOf(highscore)
        #         data_file.write(winner_id)
        #         # print("episode winnner:", winner_id)
        #     elif row.get_attribute("class") == "tmtablegrandtotal":
        #         final_scores= row.find_elements(By.TAG_NAME, "td")
        #         highscore = row.find_element(By.CLASS_NAME, "tmtablewinner").text
        #         winner_id = final_scores.indexOf(highscore)
        #         data_file.write(winner_id)
        #         # print("episode winnner:", winner_id)
        #     else:
        #         #get all children of the row
        #         columns = row.find_elements(By.TAG_NAME, "td")
        #         # get the episode number
        #         episode_num = columns[0].text
        #         # get the task description
        #         task_description = columns[1].text
        #         # get the scores for each contestant
        #         scores = columns[2:]
        #         data_file.write(episode_num)
        #         data_file.write(task_description)
        #         data_file.write(scores)
        #         # print ("episode number:", episode_num)
        #         # print ("task description:", task_description)
        #         # print ("scores:", scores)
        data_file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    data_file.close()
