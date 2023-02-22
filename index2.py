Шfrom selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager 
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup as Bs
service = ChromeService(executable_path=ChromeDriverManager().install())
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(service=service,options=op)
driver.get("https://everynoise.com")
driver.implicitly_wait(5)
driver.maximize_window()
time.sleep(2)
element = driver.find_element(By.XPATH, "/html/body/iframe")
driver.switch_to.frame(element)
bar = driver.find_element(By.XPATH, "/html/body/form/input[1]")
strinG=input()
bar.send_keys(strinG)
bar.submit()
link = driver.find_element(By.XPATH, "/html/body/div/a[@title=\"go to the profile for this artist\"]")
string = link.get_attribute("href")
driver = webdriver.Chrome(service=service,options=op)
driver.get(string)
driver.set_window_size(1024, 600)
driver.implicitly_wait(5)
driver.maximize_window()
data = driver.find_elements(By.XPATH, "//*[@id=\"alltracks\"]/div[2]/table/tbody/tr")
length = len(data)
songs_list = list()
data1 = []
for i in range(length):
    data = driver.find_element(By.XPATH, f"//*[@id=\"alltracks\"]/div[2]/table/tbody/tr[{i + 1}]/td[4]/a")
    data_list = list()
    songs_list.append(data_list)
    data1.append([strinG, data.text,data.get_attribute('href')])
dataEx = pd.DataFrame(data1, columns=[strinG,"text", "preview"])
wb = pd.ExcelWriter('FromPython.xlsx', engine='xlsxwriter')
dataEx.to_excel(wb, sheet_name='dr')
for column in dataEx:
   col_index = dataEx.columns.get_loc(column)
   wb.sheets['dr'].set_column(col_index, col_index, 40)
wb.save()
   