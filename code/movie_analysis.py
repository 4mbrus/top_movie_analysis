import pandas as pd
import matplotlib.pyplot as plt

path = "C:/Users/Ambrus/OneDrive - Central European University (CEU GmbH Hungarian Branch Office)/top_movie_analysis"

df = pd.read_csv(f"{path}/raw/top250movies.csv")

year_list = [x for x in range(1920, 2026)]

movies_per_year = df["Year"].value_counts()
movies_per_year = movies_per_year.sort_index(ascending=True)
zero_years = pd.Series([0]*len(set(year_list)-set(movies_per_year.index)), index = list(set(year_list)-set(movies_per_year.index)))

movies_per_year = pd.concat([movies_per_year, zero_years]).sort_index(ascending=True)

print(movies_per_year)

# Best year for movies
movies_per_year.plot(kind='bar', figsize=(17,5), color='pink')
plt.show()

# Best decade for movies
decade_list = [x for x in range(1920, 2030, 10)]

for year in df["Year"]:
    for decade in decade_list:
        if year >= decade and year < decade + 10:
            df.loc[df["Year"] == year, "Decade"] = f"{decade}s"

df.loc[df["Year"] >= 2020, "Decade"] = "2020s*"

fig, ax = plt.subplots(figsize=(10,5))
ax.bar( df["Decade"].value_counts().sort_index(ascending=True).index, df["Decade"].value_counts().sort_index(ascending=True), width=0.8, color='lightblue')
plt.show()
print("2020s* only includes movies from 2020-2025")

# Some more descriptive statistics
print(f"Mean year of top 250 movies: {df['Year'].mean()}")
print(f"Median year of top 250 movies: {df['Year'].median()}")
print(f"Oldest movie in top 250: {df['Year'].min()}")
print(f"Newest movie in top 250: {df['Year'].max()}")
print(f"Year with most movies in top 250: {movies_per_year.idxmax()} with {movies_per_year.max()} movies")
print(f"Mean rating of top 250 movies: {df['Score'].mean()}")
print(f"Median rating of top 250 movies: {df['Score'].median()}")
print(f"Highest rated and highest ranked movie in top 250: {df.loc[df['Score'].idxmax()]['Title']} with a rating of {df['Score'].max()} in {df[df['Score'] == df['Score'].max()].index[0]+1}th place")
print(f"Lowest rated movie in top 250: {df.loc[df['Score'].idxmin()]['Title']} with a rating of {df['Score'].min()} in {df[df['Score'] == df['Score'].min()].index[0]+1}th place")