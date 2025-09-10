
'''
EXERCISES FOR CLASS 2
'''

import numpy as np

'''
Exercise 1

Create a list of your favorite fruits and print each fruit on a new line using a for loop.

'''
favorite_fruits = ["Apple", "Banana", "Orange", "Grapes", "Strawberry"]

for fruit in favorite_fruits:
    print(fruit)

'''
Exercise 2

Create a set of your favorite colors and print the length of the set.

'''
favorite_colors = {"Red", "Blue", "Green", "Yellow", "Purple"}

print("Length of favorite colors set:", len(favorite_colors))

'''
Exercise 3

Create a dictionary of your favorite movies and their ratings out of 10. 
Print the rating of your favorite movie.

'''
favorite_movies = {"Movie1": 8, "Movie2": 9, "Movie3": 7}

print("Rating of my favorite movie:", favorite_movies["Movie2"])

'''
Exercise 4

Create a list of numbers and print the square of each number using a for loop.

'''
numbers_list = [2, 5, 7, 10, 3]

for num in numbers_list:
    print(f"Square of {num}: {num**2}")

'''
Exercise 5

Create one one-dimensional numpy array,  with 5 elements of your choice and of any type. 
Then, add an element, remove and element, and change an element.

'''
numpy_array = np.array([1, 2, 3, 4, 5])
print("Original Array:", numpy_array)

numpy_array = np.append(numpy_array, 6)
print("Array after adding element:", numpy_array)

numpy_array = np.delete(numpy_array, 2)
print("Array after removing element:", numpy_array)

numpy_array[1] = 8
print("Array after changing element:", numpy_array)


'''
Exercise 6

Create a program that generates a list of the first 10 square numbers (1, 4, 9, ...).

'''
square_numbers = [i**2 for i in range(1, 11)]
print("List of the first 10 square numbers:", square_numbers)


'''
Exercise 7

Create a program that calculates the average of a list of numbers.

'''
numbers_to_average = [2, 4, 6, 8, 10]
average = sum(numbers_to_average) / len(numbers_to_average)
print("Average of numbers:", average)


'''
Exercise 8

Create a list of numbers. Write a program that prints all the even numbers in the list.

'''
numbers_to_check_even = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers_to_check_even:
    if num % 2 == 0:
        print(num)


'''
Exercise 9

Create a dictionary representing a person with keys for "name", "age", and "city". 
Print each key-value pair in the dictionary.

'''
person_dict = {"name": "John", "age": 25, "city": "New York"}

for key, value in person_dict.items():
    print(f"{key}: {value}")


'''
Exercise 10

Write a program that calculates the total price of items in a shopping cart. 
Use a dictionary to represent the items and their prices.

'''
shopping_cart = {"item1": 20, "item2": 30, "item3": 15}
total_price = sum(shopping_cart.values())
print("Total price of items in the shopping cart:", total_price)


'''
Exercise 11

Create a program that removes duplicate elements from a list and converts it to a set.

'''
numbers_with_duplicates = [1, 2, 3, 4, 3, 2, 5, 6, 7, 8, 7, 6]
unique_numbers_set = set(numbers_with_duplicates)
print("Unique numbers:", list(unique_numbers_set))


'''
Exercise 12

Create a program that computes the average of the unique values present in the following list:

my_list = [1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8]

'''
my_list = [1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8]
unique_values = list(set(my_list))
average_unique_values = sum(unique_values) / len(unique_values)
print("Average of unique values:", average_unique_values)


'''
Exercise 13

Create a program that finds the maximum and minimum values in a given NumPy array.
Use the following list as an example:

my_list = [1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8]

'''
my_list_for_numpy = [1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8]
numpy_array_for_max_min = np.array(my_list_for_numpy)

max_value = np.max(numpy_array_for_max_min)
min_value = np.min(numpy_array_for_max_min)

print("Maximum value:", max_value)
print("Minimum value:", min_value)


'''
Exercise 14

Create a NumPy array with values from 1 to 10. 
Print the array.

'''
numpy_array_1_to_10 = np.arange(1, 11)
print("NumPy array:", numpy_array_1_to_10)


'''
Exercise 15

Write a program that slices a NumPy array to extract the subarray [3, 4, 5].
Use the following list as an example:

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
my_list_for_slice = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numpy_array_for_slice = np.array(my_list_for_slice)
subarray = numpy_array_for_slice[2:5]
print("Subarray [3, 4, 5]:", subarray)


'''
Exercise 16

Create a list of dictionaries, where each dictionary represents a person with keys for "name" and "age". 
Print the names of all individuals in the list.

'''
people_list = [
    {"name": "Alice", "age": 28},
    {"name": "Bob", "age": 35},
    {"name": "Charlie", "age": 22}
]

for person in people_list:
    print("Name:", person["name"])


'''
Exercise 17

Write a program that takes a list of dictionaries representing books with keys for "title" and "author". 
Allow the user to input a book title, and print the author of that book if it exists in the list.

'''
books_list = [
    {"title": "Book1", "author": "Author1"},
    {"title": "Book2", "author": "Author2"},
    {"title": "Book3", "author": "Author3"}
]

book_title_input = input("Enter a book title: ")
for book in books_list:
    if book["title"] == book_title_input:
        print("Author:", book["author"])
        break
else:
    print("Book not found")

'''
Exercise 18

Create a program that generates a list of dictionaries, each representing a student with keys for "name" and "grades". 
Calculate and print the average grade for each student.

'''
students_list = [
    {"name": "Student1", "grades": [90, 85, 92]},
    {"name": "Student2", "grades": [78, 88, 95]},
    {"name": "Student3", "grades": [85, 90, 88]}
]

for student in students_list:
    average_grade = sum(student["grades"]) / len(student["grades"])
    print(f"{student['name']}'s average grade: {average_grade}")


'''
Exercise 19

Write a program that takes a list of dictionaries representing products with keys for "name" and "price". 
Calculate and print the total cost of all products.

'''
products_list = [
    {"name": "Product1", "price": 20},
    {"name": "Product2", "price": 30},
    {"name": "Product3", "price": 15}
]

total_cost = sum(product["price"] for product in products_list)
print("Total cost of products:", total_cost)


'''
Exercise 20

Write a program that accepts a list of dictionaries representing cars with keys for "brand" and "year". 
Print the brands of all cars that are from the year 2020.

Use the following list as an example:

cars_list = [
    {"brand": "Toyota", "year": 2020},
    {"brand": "Honda", "year": 2019},
    {"brand": "Ford", "year": 2020}
]

'''
cars_list = [
    {"brand": "Toyota", "year": 2020},
    {"brand": "Honda", "year": 2019},
    {"brand": "Ford", "year": 2020}
]

for car in cars_list:
    if car["year"] == 2020:
        print("Brand of car from 2020:", car["brand"])