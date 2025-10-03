import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from bs4  import BeautifulSoup
import requests

URL = "https://editorial.rottentomatoes.com/guide/best-movies-of-all-time/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

top250 = pd.DataFrame()
title_list = []
year_list = []

titles = soup.find_all('a', class_='title')

for t in titles:
    title_list.append(t.get_text())

top250['Title'] = title_list


years = soup.find_all('span', class_='year')

for y in years:
    year_list.append(y.get_text())

top250['Year'] = year_list

print(top250.head())