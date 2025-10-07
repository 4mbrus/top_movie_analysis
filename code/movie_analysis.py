import pandas as pd
import matplotlib.pyplot as plt

path = "C:/Users/Ambrus/OneDrive - Central European University (CEU GmbH Hungarian Branch Office)/top_movie_analysis" # Change this to your own path

df = pd.read_csv(f"{path}/raw/top300movies.csv")

year_list = [x for x in range(1920, 2026)]

movies_per_year = df["Year"].value_counts()
movies_per_year = movies_per_year.sort_index(ascending=True)
zero_years = pd.Series([0]*len(set(year_list)-set(movies_per_year.index)), index = list(set(year_list)-set(movies_per_year.index))) # Adding years with zero movies to the series, to have a continuous x axis

movies_per_year = pd.concat([movies_per_year, zero_years]).sort_index(ascending=True) # Adding the zero years to the original series, and sorting by year

# Plot best year for movies
movies_per_year.plot(kind='bar', figsize=(17,5), color='pink', title="Number of top 300 movies per year")
plt.savefig(f"{path}/output/movies_per_year.png")

# Create dataframe for best decades for movies
decade_list = [x for x in range(1920, 2030, 10)]

for year in df["Year"]:
    for decade in decade_list:
        if year >= decade and year < decade + 10:
            df.loc[df["Year"] == year, "Decade"] = f"{decade}s"

df.loc[df["Year"] >= 2020, "Decade"] = "2020s*" # Special case for 2020s, as the decade is not over yet

movies_per_decade = df["Decade"].value_counts().sort_index(ascending=True)

# Plot best decade for movies
fig, ax = plt.subplots(figsize=(17,5))
movies_per_decade.plot(kind='bar', color='lightblue', title="Number of top 300 movies per decade",)
plt.savefig(f"{path}/output/movies_per_decade.png")

# Some more descriptive statistics, and saving them to a markdown file
statistics_md = f"{path}/output/results.md"
with open(statistics_md, "w") as f:
    f.write("# Some descriptive statistics about the top 300 movies:\n\n")
    f.write(f"- Mean year of top 300 movies: {round(df['Year'].mean(),2)}\n")
    f.write(f"- Median year of top 300 movies: {df['Year'].median()}\n")
    f.write(f"- Oldest movie in top 300: {df['Year'].min()}, {df.loc[df['Year'].idxmin()]['Title']} (in case of multiple movies from that year, the highest ranked)\n")
    f.write(f"- Newest movie in top 300: {df['Year'].max()}, {df.loc[df['Year'].idxmax()]['Title']} (in case of multiple movies from that year, the highest ranked)\n")
    f.write(f"- Year with most movies in top 300: {movies_per_year.idxmax()} with {movies_per_year.max()} movies\n")
    f.write(f"- Mean rating of top 300 movies: {round(df['Score'].mean(),2)}\n")
    f.write(f"- Median rating of top 300 movies: {df['Score'].median()}\n")
    f.write(f"- Highest rated and highest ranked movie in top 300: {df.loc[df['Score'].idxmax()]['Title']} with a rating of {df.loc[df['Score'].idxmax()]['Rank']}th place\n")
    f.write(f"- Lowest rated movie in top 300: {df.loc[df['Score'].idxmin()]['Title']} with a rating of {df['Score'].min()} in {df.loc[df['Score'].idxmin()]['Rank']}th place\n")
    f.write(f"\n![Number of top 300 movies per year plot](./movies_per_year.png)\n")
    f.write(f"![Number of top 300 movies per decade plot](./movies_per_decade.png)\n")
    f.write(f"\n\*Note: The 2020s decade only includes movies from 2020-2025 as the dataset was created in 2025.*\n")
