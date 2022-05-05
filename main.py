from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(START_URL)
print(page)
soup = BeautifulSoup(page.text, "html.parser")
star_table = soup.find('table')
time.sleep(10)
headers = ["Proper name", "Distance" , "Mass" , "Radius"]
planet_data = []

table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    planet_data.append(row)

Star_names = []
Distance = []
Mass = []
Radius = []

for i in range(1,len(planet_data)): 
    Star_names.append(planet_data[i][1]) 
    Distance.append(planet_data[i][3]) 
    Mass.append(planet_data[i][5]) 
    Radius.append(planet_data[i][6]) 
    
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)),columns=['Star_name','Distance','Mass','Radius']) 
print(df2) 
df2.to_csv('bright_stars.csv')