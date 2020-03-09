import pandas as pd
import requests
from bs4 import BeautifulSoup


page = requests.get('https://forecast.weather.gov/MapClick.php?lat=39.74001000000004&lon=-104.99201999999997')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')
# print(week)


#----- NEXT STEP ---------
# get items from main container, below
items = week.find_all(class_='tombstone-container')

# print(items) #<-- all items
# print(items[0])  #<-- first item


#----- NEXT STEP ---------
# get all days from period-name class, below  (list comprehension)
period_names = [item.find(class_='period-name').get_text() for item in items]

# get all descriptions from short-desc class, below  (list comprehension)
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]

# get all temperatures from temp class, below  (list comprehension)
temperatures = [item.find(class_='temp').get_text() for item in items]

# print(period_names) 
# print(short_descriptions)
# print(temperatures)


#----- NEXT STEP ---------
# use of pandas to put data into nice tables for import to excel spreadsheets
# dictionary with key: value column names
weather_info = pd.DataFrame({
    'period': period_names,
    'short_descriptions': short_descriptions,
    'temperatures': temperatures
})

print(weather_info)


#----- NEXT STEP ---------
# export pandas table data to csv file automatically
weather_info.to_csv('weather.csv')