import pandas as pd
from bs4  import BeautifulSoup
import requests

path = "C:/Users/Ambrus/OneDrive - Central European University (CEU GmbH Hungarian Branch Office)/top_movie_analysis" # Change this to your own path
URL = "https://editorial.rottentomatoes.com/guide/best-movies-of-all-time/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

#Create dataframe

top300 = pd.DataFrame()
title_list = []
year_list = []
score_list = []

#Create lists for titles, years, and scores

titles = soup.find_all('a', class_='title')
for t in titles:
    title_list.append(t.get_text())
top300['Title'] = title_list

years = soup.find_all('span', class_='year')
for y in years:
    year_list.append(y.get_text())
top300['Year'] = year_list

scores = soup.find_all('span', class_='score')
for s in scores:
    score_list.append(s.get_text())
top300['Score'] = score_list

#Clean data
top300['Title'] = top300['Title'].str.strip().astype(str)
top300['Year'] = top300['Year'].str.replace('(', '').str.replace(')', '').astype(int)
top300['Score'] = top300['Score'].str.replace('%', '').astype(int)

#Save to CSV
top300.to_csv(f'{path}/raw/top300movies.csv', index=False)
print(f"Saved top 300 movies to {path}/raw/top300movies.csv")