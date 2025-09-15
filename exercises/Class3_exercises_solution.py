
'''
EXERCISES FOR CLASS 3
'''
import pandas as pd

'''
Exercise 1

Create a DataFrame with the following data:

     Name  Age  Gender
0    John   25    Male
1    Mary   32  Female
2  Joseph   19    Male
3    Lisa   41  Female

'''
data = {'Name': ['John', 'Mary', 'Joseph', 'Lisa'],
        'Age': [25, 32, 19, 41],
        'Gender': ['Male', 'Female', 'Male', 'Female']}
df = pd.DataFrame(data)
print(df)

'''
Exercise 2
Using the DataFrame from Exercise 1, access the following:

The entire 'Name' column.
The 'Age' value for 'Lisa'.
The row for 'Joseph'.

'''
print("Entire 'Name' column:")
print(df['Name'])

print("'Age' value for 'Lisa':")
print(df.loc[df['Name'] == 'Lisa', 'Age'])

print("Row for 'Joseph':")
print(df.loc[df['Name'] == 'Joseph'])

'''
Exercise 3

Using the DataFrame from Exercise 1, change the column name 'Age' to 'Years'.

'''
df = df.rename(columns={'Age': 'Years'})
print(df)

'''
Exercise 4

Using the DataFrame from Exercise 1, add a new row for 'Emily', age 28, and gender 'Female'. 
Also, add a new column called 'Salary' with values [50000, 60000, 35000, 80000, 45000].

'''
new_row = {'Name': 'Emily', 'Years': 28, 'Gender': 'Female', 'Salary': 50000}
df = df._append(new_row, ignore_index=True)
df['Salary'] = [50000, 60000, 35000, 80000, 45000]
print(df)

'''
Exercise 5

Using the DataFrame from Exercise 4, remove the row for 'Joseph' and the column for 'Gender'.

'''
df = df[df['Name'] != 'Joseph']
df = df.drop(columns=['Gender'])
print(df)

'''
Exercise 6

Using the DataFrame from Exercise 4, change the 'Salary' value for 'Mary' to 65000.

'''
df.loc[df['Name'] == 'Mary', 'Salary'] = 65000
print(df)

'''
Exercise 7

Add a column to the DataFrame named "Age in 10 years", that result from adding 10 to each age

'''
df['Age in 10 years'] = df['Years'] + 10
print(df)

'''
Exercise 8

Remove the column created in exercise 7 a remove the record of "Joseph" from the DataFrame

'''
df = df.drop(columns=['Age in 10 years'])
df = df[df['Name'] != 'Joseph']
print(df)

'''
Exercise 9

Read the csv file "dataset" to a pandas dataframe and get information about the dataset 
(null values, types of data, shape, column names...)

'''
dataset_df = pd.read_csv("dataset.csv")
print(dataset_df.info())

'''
Exercise 10

Drop the missing values

'''
dataset_df = dataset_df.dropna()
print(dataset_df)

'''
Exercise 11

Sort in descendant order the dataframe by column 1

'''
dataset_df = dataset_df.sort_values(by='col1', ascending=False)
print(dataset_df)

'''
Exercise 12

Filter the DataFrame according to following conditions:
1. The values of 'col1' must be greater or equal than 2
2. The values of 'col2' must be less than 13
3. The values of 'col6' must contain the letters 'F', 'G', and 'J'
Export the DataFrame to an excel file named "new_dataset"
'''
filtered_df = dataset_df[(dataset_df['col1'] >= 2) & (dataset_df['col2'] < 13) & dataset_df['col6'].str.contains('F|G|J')]
filtered_df.to_excel("new_dataset.xlsx", index=False)


'''
Exercise 13

Write a program that reads a CSV file containing information about books with columns for "Title", "Author", and "Price". 
Print the DataFrame.

'''
books_df = pd.read_csv("books_info.csv")
print(books_df)


'''
Exercise 14

Create a program that generates a DataFrame representing a list of employees with columns for "Name", "Department", and "Salary". 
Print the names of all employees in the DataFrame.

'''
employees_data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Department": ["HR", "IT", "Finance"],
    "Salary": [55000, 60000, 50000]
}

employees_df = pd.DataFrame(employees_data)
print("Names of employees:")
print(employees_df["Name"])


'''
Exercise 15

Write a program that creates and filters a given DataFrame to show only the rows where the price of a product is greater than 50.
You should create the Pandas Dataframe with the columns "Product", "Price", and "Quantity".

'''
products_df = pd.DataFrame({
    "Product": ["A", "B", "C", "D"],
    "Price": [60, 30, 80, 40],
    "Quantity": [10, 5, 8, 12]
})
filtered_products_df = products_df[products_df['Price'] > 50]
print(filtered_products_df)


'''
Exercise 16

Write a program that saves the DataFrame from Exercise 15 to a CSV file.

'''
filtered_products_df.to_csv("filtered_products.csv", index=False)


'''
Exercise 17

Write a program that orders the DataFrame from Exercise 15 from the most expensive Product to the least expensive.

'''
sorted_products_df = products_df.sort_values(by='Price', ascending=False)
print(sorted_products_df)


'''
Exercise 18

Write a program that removes the most expensive product from Exercise 15 Dataframe.

'''
most_expensive_product = sorted_products_df.iloc[0]
products_df = products_df[products_df['Product'] != most_expensive_product['Product']]
print(products_df)


'''
Exercise 19

Write a program that puts all of the records in Exercise 15 Dataframe into a single list.

'''
records_list = products_df.values.tolist()
print(records_list)


'''
Exercise 20

Use the resulting list from Exercise 19 to generate the same Pandas DataFrame that you created in Exercise 15.

'''
new_df_from_list = pd.DataFrame(records_list, columns=products_df.columns)
print(new_df_from_list)
