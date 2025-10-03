import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from bs4  import BeautifulSoup
import requests

path = "C:/Users/Ambrus/OneDrive/top_movie_analysis"
URL = "https://editorial.rottentomatoes.com/guide/best-movies-of-all-time/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

#Create dataframe

top250 = pd.DataFrame()
title_list = []
year_list = []
score_list = []

#Create lists for titles, years, and scores

titles = soup.find_all('a', class_='title')
for t in titles:
    title_list.append(t.get_text())
top250['Title'] = title_list

years = soup.find_all('span', class_='year')
for y in years:
    year_list.append(y.get_text())
top250['Year'] = year_list

scores = soup.find_all('span', class_='score')
for s in scores:
    score_list.append(s.get_text())
top250['Score'] = score_list

#Clean data
top250['Year'] = top250['Year'].str.replace('(', '').str.replace(')', '').astype(int)
top250['Score'] = top250['Score'].str.replace('%', '').astype(int)

#Save to CSV
top250.to_csv(f'{path}/raw/top250movies.csv', index=False)
