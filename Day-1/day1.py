# python version

# command: python3 --version
# Python 3.12.4

print("Hello World!!!")  # Hello World!!! 
# toRUN: right click --> Run Python or trianglr button on left top corner.


# Python does not require you to declare variable types explicitly — it automatically determines the type based on the assigned value.
'''name = "Alice"
age = 30
is_developer = True'''

# name stores a string("Alice").
# age stores an integer(30).
# is_developer stores a boolean value(True).

# ------------------------------------------------------------------------------------------

# DATA TYPES
# Integer(int): Whole numbers, e.g., 1, 100, -5.
# Float(float): Numbers with a decimal point, e.g., 3.14, -0.5.
# String(str): Text, e.g., "Hello", "Python".
# Boolean(bool): True or False.
# None: Represents the absence of a value.

'''x = 10          # Integer
y = 3.14        # Float
name = "John"   # String
is_active = True  # Boolean


print(x) #10
print(y) #3.14
print(name) #John
print(is_active)  #True '''

#---------------------------------------------------------------------------------------------

# SIMPLE OPERATIONS
# Python supports arithmetic operations like addition, subtraction, multiplication, and division.

'''a = 10
b = 5

# Arithmetic operations
sum_result = a + b      # Addition
diff_result = a - b     # Subtraction
prod_result = a * b     # Multiplication
div_result = a / b      # Division (result will be float)

print("Sum:", sum_result)            # Sum: 15
print("Difference:", diff_result)    # Difference: 5
print("Product:", prod_result)       # Product: 50
print("Division:", div_result)       # Division: 2.0 '''

#---------------------------------------------------------------------------------------

# PRINT STATEMENT -- print()
# We use the print() function to display output in Python.

'''name = "Alice"
age = 30

print("Name:", name)  # Name: Alice
print("Age:", age)    # Age: 30'''

#---------------------------------------------------------------------------------------------

# ASKING FOR USER INPUT
# input() is used to take input from the user.  -- takes value in form of strings
# f"{}" is an f-string, a convenient way to embed variables into strings.

# Asking for user input
'''name = input("Enter your name: ") # Atul
age = input("Enter your age: ")   #24

# Displaying the message
print(f"Hello, {name}! You are {age} years old.")   #Hello, Atul! You are 24 years old. '''

#----------------------------------------------------------------------------------------------------

# HOMEWORK 
# Write a program that asks the user to enter two numbers, and then prints the result of adding, subtracting, multiplying, and dividing those numbers.
# Hint: Use input() to get the numbers and convert them to int using int().
# Experiment with different data types and print their types using the type() function.

'''x = input()
print(type(x))
x=int(x)
print(type(x))

y = input()
print(type(y))
y = int(y)
print(type(y))

print(x+y)
print(type(x+y))

print(x-y)
print(type(x-y))

print(x*y)
print(type(x*y))

print(x/y)
print(type(x/y))'''


#------------------------------------------------------------------------------------


# ------ Lists and Tuples: Basic Introduction ----------

# 1. Lists
#     A list is a collection of items that can hold multiple values.
#     Lists are ordered(the order of elements matters), mutable(can be changed), and can contain elements of different data types.
#     Lists are created using square brackets[].
#     You can access list elements using their index, starting from 0.

'''
#DECLARATION
my_list = [1, 2, 3, 4, 5]  # A list of integers
names = ["Alice", "Bob", "Charlie"]  # A list of strings
mixed_list = [1, "Alice", True, 3.14]  # A list with mixed data types

#ACCESSING
print(my_list)
print(my_list[0])  # Output: 1 (first element)
print(names[1])    # Output: Bob (second element)


#MODIFYING
my_list[0] = 10  # Changing the first element to 10
print(my_list)    # Output: [10(modified), 2, 3, 4, 5]
'''


# 2. Tuples
#    A tuple is also a collection of items, but unlike lists, tuples are immutable(they cannot be changed after creation).
#    Tuples are used when you want a sequence of items that shouldn’t be modified.
#    Tuples are created using parentheses().
#    You can access tuple elements just like you do with lists.

'''
# DECLARATION
my_tuple = (1, 2, 3, 4, 5)  # A tuple of integers
names_tuple = ("Alice", "Bob", "Charlie")  # A tuple of strings

# ACCESSING
print(my_tuple[0])  # Output: 1
print(names_tuple[1])  # Output: Bob

# MODIFICATION (NOT ALLOWED)
# This will cause an error:
my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment
'''


# Key Differences Between Lists and Tuples:
#   Lists: Mutable(can be changed), defined with square brackets[].
#   Tuples: Immutable(cannot be changed), defined with parentheses().


#---------------------------------------------------------------------------------------------------------

# Practice Exercises

# 1. List Exercise:
# Create a list of 5 different fruits.
# Print the list, change the second fruit to something else, and then print the modified list.

'''
fruits=["Apple","Banana","Mango","Pear","Orange"]
print(fruits)
fruits[1] = "Watermelon"
print(fruits)
'''


# 2. Tuple Exercise:
# Create a tuple that contains 3 numbers.
# Print the tuple and access the second number.
# Try to modify an element (and observe the error message).

'''
num = (1,2,3)
print(num)
print(num[1])
# num[1]=10  # TypeError: 'tuple' object does not support item assignment
'''






