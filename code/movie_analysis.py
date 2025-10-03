import pandas as pd
import matplotlib.pyplot as plt
path = "C:/Users/Ambrus/OneDrive - Central European University (CEU GmbH Hungarian Branch Office)/top_movie_analysis"

df = pd.read_csv(f"{path}/raw/top250movies.csv")

year_list = [x for x in range(1920, 2025)]

movies_per_year = df["Year"].value_counts().sort_index(ascending=False)
movies_per_year = movies_per_year.sort_index(ascending=True)
print(movies_per_year)
