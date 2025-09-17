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


'''
Exercise 2

Select the first 10 rows of the columns Generosity and Residual.
'''
# ANSWER


'''
Exercise 3

Print the mean of the column Score using pandas.
'''
# ANSWER


'''
Exercise 4

Print the mean of the column Score using an SQL query.
'''
# ANSWER


'''
Exercise 5

Create a query to filter the Country column where the Score is greater than 5. 
Do not modify the original table; Use select and print the result using a dataframe.
'''
# ANSWER


'''
Exercise 6

From the filtered dataframe in the previous exercise, 
order the rows by Score (descending) and show the first 10 rows.
'''
# ANSWER


'''
Exercise 7

Check if Portugal is in the filtered dataframe and print its score if found.
'''
# ANSWER


'''
Exercise 8

Using pandas, count the number of unique countries in the dataset.
'''
# ANSWER


'''
Exercise 9

Using SQL, find the top 5 countries with the highest GDP_Per_Capita.
'''
# ANSWER


'''
Exercise 10

Using SQ cursor, find the bottom 5 countries with the lowest Healthy_Life_Expectancy.
'''
# ANSWER


'''
Exercise 11

Find the maximum and minimum values of the Score column using SQL.
'''
# ANSWER


'''
Exercise 12

Select all countries where the Generosity is greater than 0.3.
'''
# ANSWER


'''
Exercise 13

Select all countries where the Country name starts with the letter 'S'.
'''
# ANSWER


'''
Exercise 14

Using pandas, compute the correlation between GDP_Per_Capita and Score.
'''
# ANSWER


'''
Exercise 15

Using SQL, group countries by their first letter
and compute the average Score per first letter.
'''
# ANSWER


'''
Exercise 16

Add a new pandas column 'Happiness_Level':
- 'High' if Score > 6
- 'Moderate' if 5 ≤ Score ≤ 6
- 'Low' if Score < 5
Print the counts of each level.
'''
# ANSWER


'''
Exercise 17

For each Happiness_Level, compute the average GDP_Per_Capita using pandas.
'''
# ANSWER


'''
Exercise 18

Export the full hapiness table into a CSV file named 'hapiness_full.csv'.
'''
# ANSWER
