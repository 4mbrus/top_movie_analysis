# Top Movies Analysis

**This project scrapes and analyses Rotten Tomatoes' "300 Best Movies of All Time" list.**

## Requirements
- Tested OS: Windows 11 24H2, Fedora Linux 42
- Tested python versions: 3.12 and 3.13
- Packages: see [environment.yml](environment.yml)
- Hardware: anything that can run python

## Data Source
[RottenTomatoes: 300 Best Movies of All Time](https://editorial.rottentomatoes.com/guide/best-movies-of-all-time)

## Folder structure

~~~
top_movie_analysis:
│   LICENSE
│   README.md
│   environment.yml
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
2. In the root folder of the project, run in terminal/Anaconda prompt: "conda env update -f environment.yml --prune" to get the necessary packages.
3. Change "path" variable in both .py files in the "code" folder
4. Run "movie_scrape.py"
5. Run "movie_analysis.py"
6. Check your results in the output folder.

## Results

The [statistics.md](/output/results.md) file contains my findings from 04.10.2025. If code is executed, all findings will be written there.

# License

MIT License

Copyright (c) 2025 4mbrus

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.