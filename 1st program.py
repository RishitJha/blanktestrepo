# #print("Hello, World!")
# #Variable#
# name = "John"
# age = 30 #value is stored from right to left
# price = 25.59
# print("Name:", name)
# print("My age:", age)
# print("Price:", price)  

# #identifier rules
# #1. Identifiers can contain letters, digits, and underscores
# #2. Identifiers cannot start with a digit
# #3. Identifiers are case-sensitive
# #4. Identifiers cannot be reserved keywords or special symbols
# # data types
# print(type(name))
# print(type(age))
# print(type(price))

# #datatypes in python
# #1. int 
# #2. float
# #3. complex
# #4. str
# name1 = "sk"
# name2 = 'sk'
# name3 = """sk"""
# print(type(name1))
# print(type(name2))
# print(type(name3))

# #5 . bool
# is_true = True
# is_false = False
# print(type(is_true))
# print(type(is_false))

# #Print Sum
# a=2
# b=5
# sum = a + b
# print("Sum:", sum)
#  #ctrl+forward slash to comment/uncomment multiple lines

# #operators
# #1. Arithmetic operators(+, -, *, /, %, **, //)
# #2. Comparison operators(==, !=, <, >, <=, >=)
# # 3. Logical operators(and, or, not)
# a = 50
# b = 30
# print(not False)  # Output: True
# print(not (a > b))  # Output: False
# val1 = True
# val2 = False    
# print("and operator:", val1 and val2)  # Output: False(needs both to work)
# print("or operator:", val1 or val2)  # Output: True(needs one to work)
# #4. Assignment operators(=, +=, -=, *=, /=, %=, **=, //=)(equal to, sum, difference, product, quotient, remainder, exponentiation, floor division)
# #. Bitwise operators(&, |, ^, ~, <<, >>)
# #assignment operators
# num = 10
# num += 5  # equivalent to num = num + 5
# num -= 3  # equivalent to num = num - 3
# num *= 2  # equivalent to num = num * 2
# num /= 4  # equivalent to num = num / 4
# num %= 3  # equivalent to num = num % 3
# num **= 2  # equivalent to num = num ** 2
# num //= 2  # equivalent to num = num // 2
# print("num:", num)

# #type conversion
# a = 2
# b = 3.5
# sum = a + b  # a is automatically converted to float
# print("Sum:", sum)

# a = "2"
# b = 3.5
# #sum = a + b #2 is interpreted as string and 3.5 is float so it will give error

# a = "2"
# b = "3"
# sum = a + b  # strings are concatenated
# print("Sum:", sum)

# #type casting
# a = float ("2")
# b = 3.5     
# print(type(a))  # Output: <class 'float'>   
# print(a + b)  # Output: 5.5

# #a = float"rishit"  #This will give an error because "rishit" cannot be converted to a float.    

# #INPUT
# input ("enter your name:")  #This will take input from the user and store it as a string.
# name = input("enter your name:")  #This will take input from the user and store it as a string.
# print ("you entered:", name)  #This will print the value of the variable name.

# #Input with type conversion
# value1 = int(input("Enter a number: "))  #This will take input from the user and convert it to an integer.
# value2 = float(input("Enter a decimal number: "))  #This will take input from
# print(type(value1))  # Output: <class 'int'>
# print(type(value2))  # Output: <class 'float'>

# #Practice  Questions:
# #1. Write a program that takes two numbers as input and prints their sum
# first = int(input("enter first number:"))
# second = int(input("enter second number:"))
# sum = first + second
# print("Sum:", sum)

# #2. input side of a square and print its area
# side = float(input("Enter the side of the square: "))
# area = side * side
# area1 = side ** 2

# #3. 2 floating numbers and print their average 

# Num1 = float(input("Enter first floating number: "))
# Num2 = float(input("Enter second flating number:"))
# Avg = (Num1 +  Num2) / 2
# print("Average:", Avg)

#4. input 2 numbers, a and b, print true ifa is greater than or equal to b, otherwise print false
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if a >= b:
    print("True")
    