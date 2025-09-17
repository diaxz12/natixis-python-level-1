'''
EXERCISES FOR CLASS 4
'''

'''
Exercise 1

Connect to the database 'database.db', that contains a dataset. 
Create a cursor and list all columns of the table 'hapiness'. 
Also create a pandas dataframe from this table.
Do not close the connection yet.
'''
# ANSWER
import sqlite3
import pandas as pd

DB_PATH = "database.db"
TABLE = 'hapiness'

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute(f"PRAGMA table_info({TABLE})")
columns = [col[1] for col in cursor.fetchall()]
print("Exercise 1 — Columns:", columns)

df = pd.read_sql_query(f"SELECT * FROM {TABLE}", conn)
print("Exercise 1 — Loaded rows:", len(df))

'''
Exercise 2

Select the first 10 rows of the columns Generosity and Residual.
'''
# ANSWER
df_top10 = pd.read_sql_query(f"SELECT Generosity, Residual FROM {TABLE} LIMIT 10", conn)
print("Exercise 2")
print(df_top10)

'''
Exercise 3

Print the mean of the column Score using pandas.
'''
# ANSWER
mean_score = df['Score'].mean()
print("Exercise 3 — Mean Score (DataFrame):", mean_score)


'''
Exercise 4

Print the mean of the column Score using an SQL query.
'''
# ANSWER
cursor.execute(f"SELECT AVG(Score) FROM {TABLE}")
mean_score_sql = cursor.fetchone()[0]
print("Exercise 4 — Mean Score (SQL):", mean_score_sql)

'''
Exercise 5

Create a query to filter the Country column where the Score is greater than 5. 
Do not modify the original table; Use select and print the result using a dataframe.
'''
# ANSWER
df_filtered = pd.read_sql_query(f"SELECT * FROM {TABLE} WHERE Score > 5", conn)
print("Exercise 5 — Countries with Score > 5")
print(df_filtered)

'''
Exercise 6

From the filtered dataframe in the previous exercise, 
order the rows by Score (descending) and show the first 10 rows.
'''
# ANSWER
df_filtered_sorted = df_filtered.sort_values(by='Score', ascending=False).head(10)
print("Exercise 6 — Top 10 Countries by Score:")
print(df_filtered_sorted)   

'''
Exercise 7

Check if Portugal is in the filtered dataframe and print its score if found.
'''
# ANSWER
portugal_score = df_filtered[df_filtered['Country'] == 'Portugal']['Score']
if not portugal_score.empty:
    print("Exercise 7 — Portugal Score:", portugal_score.values[0])
else:
    print("Exercise 7 — Portugal not found.")

'''
Exercise 8

Using pandas, count the number of unique countries in the dataset.
'''
# ANSWER
unique_countries = df['Country'].nunique()
print("Exercise 8 — Unique Countries:", unique_countries)

'''
Exercise 9

Using SQL, find the top 5 countries with the highest GDP_Per_Capita.
'''
# ANSWER
df_top5_gdp = pd.read_sql_query(f"SELECT Country, GDP_Per_Capita FROM {TABLE} ORDER BY GDP_Per_Capita DESC LIMIT 5", conn)
print("Exercise 9 — Top 5 Countries by GDP_Per_Capita:")
print(df_top5_gdp)

'''
Exercise 10

Using SQ cursor, find the bottom 5 countries with the lowest Healthy_Life_Expectancy.
'''
# ANSWER
cursor.execute(f"SELECT Country, Healthy_Life_Expectancy FROM {TABLE} ORDER BY Healthy_Life_Expectancy ASC LIMIT 5")
bottom5_health = cursor.fetchall()
print("Exercise 10 — Bottom 5 Countries by Healthy_Life_Expectancy:")
for country, health in bottom5_health:
    print(f" - {country}: {health}")

'''
Exercise 11

Find the maximum and minimum values of the Score column using SQL.
'''
# ANSWER
cursor.execute(f"SELECT MAX(Score), MIN(Score) FROM {TABLE}")
max_min_score = cursor.fetchone()
print("Exercise 11 — Max Score (SQL):", max_min_score[0])
print("Exercise 11 — Min Score (SQL):", max_min_score[1])

'''
Exercise 12

Select all countries where the Generosity is greater than 0.3.
'''
# ANSWER
df_generosity = pd.read_sql_query(f"SELECT * FROM {TABLE} WHERE Generosity > 0.3", conn)
print("Exercise 12 — Countries with Generosity > 0.3:")
print(df_generosity)

'''
Exercise 13

Select all countries where the Country name starts with the letter 'S'.
'''
# ANSWER
df_countries_s = pd.read_sql_query(f"SELECT * FROM {TABLE} WHERE Country LIKE 'S%'", conn)
print("Exercise 13 — Countries starting with 'S':")
print(df_countries_s)

'''
Exercise 14

Using pandas, compute the correlation between GDP_Per_Capita and Score.
'''
# ANSWER
correlation = df['GDP_Per_Capita'].corr(df['Score'])
print("Exercise 14 — Correlation between GDP_Per_Capita and Score:", correlation)


'''
Exercise 15

Using SQL, group countries by their first letter
and compute the average Score per first letter.
'''
# ANSWER
cursor.execute(f"SELECT SUBSTR(Country, 1, 1) AS First_Letter, AVG(Score) AS Avg_Score FROM {TABLE} GROUP BY First_Letter")
grouped_scores = cursor.fetchall()
print("Exercise 15 — Average Score by First Letter of Country:")
for first_letter, avg_score in grouped_scores:
    print(f" - {first_letter}: {avg_score}")

'''
Exercise 16

Add a new pandas column 'Happiness_Level':
- 'High' if Score > 6
- 'Moderate' if 5 ≤ Score ≤ 6
- 'Low' if Score < 5
Print the counts of each level.
'''
# ANSWER
def happiness_level(score):
    if score > 6:
        return 'High'
    elif 5 <= score <= 6:
        return 'Moderate'
    else:
        return 'Low'
df['Happiness_Level'] = df['Score'].apply(happiness_level)
level_counts = df['Happiness_Level'].value_counts()
print("Exercise 16 — Happiness Level Counts:")
print(level_counts)


'''
Exercise 17

For each Happiness_Level, compute the average GDP_Per_Capita using pandas.
'''
# ANSWER
avg_gdp_by_level = df.groupby('Happiness_Level')['GDP_Per_Capita'].mean()
print("Exercise 17 — Average GDP_Per_Capita by Happiness Level:")
print(avg_gdp_by_level)

'''
Exercise 18

Export the full hapiness table into a CSV file named 'hapiness_full.csv'.
'''
# ANSWER
df.to_csv('hapiness_full.csv', index=False)

