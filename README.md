# Popular_Baby_Names_SSN
State-specific data on the relative frequency of given names in the population of U.S. births where the individual has a Social Security Number (Tabulated based on Social Security records as of March 5, 2017). US Social Security applications are a great way to track trends in how babies born in the US are named. For each of the 50 states and the District of Columbia we created a file called SC.txt, where SC is the state's postal code. Each record in a file has the format: 2-digit state code, sex (M = male or F = female), 4-digit year of birth (starting with 1910), the 2-15 character name, and the number of occurrences of the name. Fields are delimited with a comma. Each file is sorted first on sex, then year of birth, and then on number of occurrences in descending order. When there is a tie on the number of occurrences names are listed in alphabetical order. This sorting makes it easy to determine a name's rank. The first record for each sex & year of birth has rank 1, the second record has rank 2, and so forth. 

To safeguard privacy, we exclude from these files certain names that would indicate, or would allow the ability to determine, names with fewer than 5 occurrences in any geographic area. If a name has less than 5 occurrences for a year of birth in any state, the sum of the state counts for that year will be less than the national count. 

## Requirements
1.	Data: https://catalog.data.gov/dataset/baby-names-from-social-security-card-applications-data-by-state-and-district-of-#topic=developers_navigation
2. Movie Dataset from Kaggle: https://www.kaggle.com/tmdb/tmdb-movie-metadata/data
3.	Python: https://www.python.org/downloads/ (if you are not familiar with Python, you may use another programming language of your choice)
4.	Tableau: https://www.tableau.com/products/desktop (you can download a free trial)

## Instructions
1.	Download the baby names and movie data from Data.gov and Kaggle
2.  Unzip the all the above files and copy the directory address of both the dataset into **merge_data.py**
3.	Programmatically merge the files into a single dataset using the **merge_data.py** script. This script will first merge all the baby names text files of 50 states into **all_states_data.csv** and later merge the movie data files into **movie_data.csv**
4.  Now you will have 2 merged dataset files after running the script. One file called  **all_states_data.csv** and other file called **movie_data.csv**
5.  For your reference, I have attached the resulting **movie_data.csv** into this repository
6.  Load both the files into Tableau and you can explore with the data and find insights
7.  Using this two datasets I have found some trends and insights which can be found in the **popular_baby_names.twbx** tableau workbook
8.  I have also attached a powerpoint presentation about the insights.

## About the Baby Names Dataset
1. The data was collected from year range: 1910 – 2016
2.  Total records after merging the files: 5,838,786
3.  The dataset consist of total 44.2% boys and 58.8% girls

## My analysis answers the following questions:
1. What is the most popular name by state by year?
2. What’s the ratio of unique boys’ and girls’ names trended over time?
3. Which names have the greatest increases and decreases (percentage difference) by year?
4. Does actor / actresses names or their character names in the movies have any impact in the popular baby names?
5. Time series analysis of baby names by gender
6. Total baby names by state and sex

## I have also created a presentation that answers the following questions:
1. Let’s say this data is updated weekly and our users would like to see a weekly
Tableau dashboard.
  * What would a potential automated solution look like?
  * What are the critical points of failure?
  * What are the resource requirements (technology, time, etc.)
2. How can a toy company can leverage this data to drive sales?
