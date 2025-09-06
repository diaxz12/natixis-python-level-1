
'''
EXERCISES FOR CLASS 1
'''


'''
Exercise 1

1. Declare a variable named my_int and assign it the value of an integer of your choice.
2. Declare a variable named my_float and assign it the value of a float of your choice.
3. Declare a variable named my_bool and assign it the value of a boolean of your choice.
4. Declare a variable named my_str and assign it the value of a string of your choice.
Once you have declared the variables, perform the following operations:
1. Print the value of my_int.
2. Print the value of my_float.
3. Print the value of my_bool.
4. Print the value of my_str.
5. Concatenate my_str with another string of your choice and print the result.

'''
my_int = 5
my_float = 3.14
my_bool = True
my_str = "Hello"

# 2. Print values
print(my_int)
print(my_float)
print(my_bool)
print(my_str)

# 3. Concatenate my_str with another string
concatenated_str = my_str + " World!"
print(concatenated_str)

'''
Exercise 2

Write a program that asks the user to enter two numbers and performs the following operations:
1.	Addition (+) of the two numbers
2.	Subtraction (-) of the two numbers
3.	Multiplication (*) of the two numbers
4.	Division (/) of the two numbers
5.	Modulus (%) of the two numbers

'''
# Program that asks the user for two numbers and performs operations
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)
print("Modulus:", num1 % num2)

'''
Exercise 3

Write a program that calculates the area and circumference of a circle using the math library. 
The program should ask the user to enter the radius of the circle.

'''
import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius**2
circumference = 2 * math.pi * radius

print("Area:", area)
print("Circumference:", circumference)

'''
Exercise 4

Create two variables of type int and assign to each variable a number of your choice. 
With the two number, perform the following operations:
1.	Checks if the first number is greater than the second number and prints a message accordingly.
2.	Checks if the second number is even and prints a message accordingly.
3.	Checks if both numbers are positive and prints a message accordingly.

'''
num_a = 8
num_b = 5

# 1.
if num_a > num_b:
    print("First number is greater than the second number")

# 2.
if num_b % 2 == 0:
    print("Second number is even")

# 3.
if num_a > 0 and num_b > 0:
    print("Both numbers are positive")

'''
Exercise 5

Create a variable name of test_score and assign it a number of your choice.
Write a program that assigns a letter grade based on the following scale:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: Below 60

'''
test_score = 85

if test_score >= 90:
    print("A")
elif test_score >= 80:
    print("B")
elif test_score >= 70:
    print("C")
elif test_score >= 60:
    print("D")
else:
    print("F")

'''
Exercise 6

Write a program that prints all the even numbers from 0 to 20 using a for loop.

'''
for num in range(0, 21, 2):
    print(num)

'''
Exercise 7

Write a program that prints all the odd numbers from 0 to 30 using a while loop.

'''
num = 1
while num <= 30:
    print(num)
    num += 2

'''
Exercise 8

Create a variable that keeps any integer number of your choice. 
Write a program that prints the multiplication table of that number from 1 to 10 using a for loop.

'''
number_for_table = 7

for i in range(1, 11):
    print(f"{number_for_table} * {i} = {number_for_table * i}")

'''
Exercise 9

Create a variable that keeps any integer positive number of your choice. 
Write a program that calculates the sum of all the numbers from 1 to that number using a while loop. 
Break the loop when the sum equals to the half of the number.

'''
number_sum = 15
sum_result = 0
current_num = 1

while current_num <= number_sum:
    sum_result += current_num
    if sum_result == number_sum / 2:
        break
    current_num += 1

print("Sum:", sum_result)


'''
Exercise 10

Fill missing pieces (____) of the following code such that prints make sense.

name = "John Doe"

if ____:
    print(f'Name "{name}" is more than 20 chars long')
    length_description = "long"
elif ____:
    print(f'Name "{name}" is more than 15 chars long')
    length_description = "semi long"
elif ____:
    print(f'Name "{name}" is more than 10 chars long')
    length_description = "semi long"
elif ____:
    print(f'Name "{name}" is 8, 9 or 10 chars long')
    length_description = "semi short"
else:
    print(f'Name "{name}" is a short name')
    length_description = "short"

'''
name = "John Doe"

if len(name) > 20:
    print(f'Name "{name}" is more than 20 chars long')
    length_description = "long"
elif len(name) > 15:
    print(f'Name "{name}" is more than 15 chars long')
    length_description = "semi long"
elif len(name) > 10:
    print(f'Name "{name}" is more than 10 chars long')
    length_description = "semi long"
elif 8 <= len(name) <= 10:
    print(f'Name "{name}" is 8, 9, or 10 chars long')
    length_description = "semi short"
else:
    print(f'Name "{name}" is a short name')
    length_description = "short"


'''
Exercise 11

Write a program that prints the first 5 multiples of 3 using a while loop.

'''
num = 3
count = 1

while count <= 5:
    print(num * count)
    count += 1


'''
Exercise 12

Create a variable with a positive integer of your choice. 
Write a program that checks whether the number is prime or not.

'''
number_to_check = 13
is_prime = True

for i in range(2, int(number_to_check/2) + 1):
    if number_to_check % i == 0:
        is_prime = False
        break

if is_prime:
    print(f"{number_to_check} is a prime number")
else:
    print(f"{number_to_check} is not a prime number")


'''
Exercise 13

Write a program that calculates the factorial of a given number using a for loop.

'''
num_factorial = 5
factorial_result = 1

for i in range(1, num_factorial + 1):
    factorial_result *= i

print(f"The factorial of {num_factorial} is {factorial_result}")


'''
Exercise 14

Write a program that prints the Fibonacci sequence up to the 10th term.

'''
fibonacci_sequence = [0, 1]

for i in range(2, 10):
    fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])

print(f"Fibonacci sequence: {fibonacci_sequence}")


'''
Exercise 15

Write a program that calculates the sum of all odd numbers from 1 to 50 using a for loop.

'''
sum_odd_numbers = 0

for num in range(1, 51, 2):
    sum_odd_numbers += num

print(f"Sum of odd numbers from 1 to 50: {sum_odd_numbers}")


'''
Exercise 16

Create a program that asks the user to input a number. 
Write a program that checks whether the number is positive, negative, or zero.

'''
user_number = int(input("Enter a number: "))

if user_number > 0:
    print("Positive")
elif user_number < 0:
    print("Negative")
else:
    print("Zero")


'''
Exercise 17

Create a program that simulates a basic calculator. 
It should ask the user for two numbers and an operator (+, -, *, /). 
Perform the corresponding operation and print the result.

'''
num1_calculator = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
num2_calculator = float(input("Enter the second number: "))

if operator == "+":
    print(num1_calculator + num2_calculator)
elif operator == "-":
    print(num1_calculator - num2_calculator)
elif operator == "*":
    print(num1_calculator * num2_calculator)
elif operator == "/":
    if num2_calculator != 0:
        print(num1_calculator / num2_calculator)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")


'''
Exercise 18

Write a program that prints the reverse of a given string.

'''
input_string = "Python"
reversed_string = input_string[::-1]
print(reversed_string)


'''
Exercise 19

Write a program that checks if a given year is a leap year. 
A leap year is divisible by 4, except for years that are divisible by 100. 
However, years divisible by 400 are leap years.

'''
year = 2000

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


'''
Exercise 20

Create a program that counts the number of vowels in "Natixis Python level 1 class." string.

'''
input_string = "Natixis Python level 1 class."
vowels = "aeiouAEIOU"
vowel_count = 0

for char in input_string:
    if char in vowels:
        vowel_count += 1

print(f"Number of vowels: {vowel_count}")