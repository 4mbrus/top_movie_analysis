# Top Movies Analysis

**This project scrapes and analyses Rotten Tomatoes' "300 Best Movies of All Time" list.**

## Requirements
See [requirements.txt](requirements.txt) for packeges used.

## Data Source
[RottenTomatoes: 300 Best Movies of All Time](https://editorial.rottentomatoes.com/guide/best-movies-of-all-time)

## Folder structure

~~~
top_movie_analysis:
│   LICENSE
│   README.md
│   requirements.txt
│
├───code
│       movie_analysis.py
│       movie_scrape.py
│
├───output
│       movies_per_decade.png
│       movies_per_year.png
│       results.md
│
└───raw
        top300movies.csv
~~~

## Reproduction

1. Clone repository
2. Change "path" variable in both .py files in the "code" folder
3. Run "movie_scrape.py"
4. Run "movie_analysis.py"
5. Check your results in the output folder.

## Results

The [statistics.md](/output/results.md) file contains my finding from 04.10.2025. If code is executed, all finding will be written there.
