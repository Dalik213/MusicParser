import pandas as pd
import requests
from bs4 import BeautifulSoup as Bs
string = input()
songs_list = list()
string = ''.join([i for i in string if i.isalpha()])
string = 'https://everynoise.com/engenremap-' + string + '.html'
r = requests.get(string)
html = Bs(r.content, 'html.parser')
data = []
for el in html.find_all("div", class_= 'genre scanme'):
   data_list = list()
   songs_list.append(data_list)
   data.append([el.text, el['title'], el['preview_url']])
   
dataEx = pd.DataFrame(data, columns=["Author", "Title", "Preview"])
wb = pd.ExcelWriter('FromPython.xlsx', engine='xlsxwriter')
dataEx.to_excel(wb, sheet_name='Sheet')
for column in dataEx:
   col_index = dataEx.columns.get_loc(column)
   wb.sheets['Sheet'].set_column(col_index, col_index, 30)
wb.save()
   