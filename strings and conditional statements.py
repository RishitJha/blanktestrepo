# str1 = "This is a sample string. \n second line of the string."
# str2 = "This is another string."
# print(str1+str2)  # Concatenation of two strings
# final_string = str1 + " " + str2  # Concatenation with a space in between
# print(final_string)  # Output: This is a sample string.
# print(len(final_string)) #also counts the length of the string including spaces and special characters

# #indexing
# str = "apna college"
# ch = str[0]  # Accessing the first character of the string
# print(ch)  # Output: a
# #str[4] = "C"  # This will give an error because strings are immutable in Python

# #Slicing(negative indexing only works for slicing)
# print(str[1 : 5])
# print(str[-5 : -1])  # Output: college

# str = "i am studying python from apna college:" 
# print(str.endswith("college:"))  # Output: True
# print(str.capitalize())  # Output: I am studying python from apna college: only works in this contexted
# print(str) #Output: i am studying python from apna college:
# print(str.replace("python", "java"))  # Output: i am studying java from apna college:
# print(str.find("python"))  # Output: 14 (index of the first occurrence of "python")
# print(str.count("a"))  # Output: 4 (number of occurrences of "a" in the string)

#Practice Questions:
#1. input a string and print its length
# name = input("Enter your name")
# print("Length of the string:", len(name))

#2 find the occureence of $ in a string
# str = "Hi, $Iam the $ symbol, $40"
# print("Number of occurrences of $:", str.count("$"))  # Output: 3

#conditional statements:
#1. if statement
# age = 23
# if (age>= 18):
#     print("You are eligible to vote.")  # Output: You are eligible to vote.

# 2. if-else statement
# light = "green"  #if statement checks the condition and executes the block of code if the condition is true. If the condition is false, it executes the else block
# if (light == "red"):
#     print("stop") #always give 4 spaces before the print for indentations, vs code automatically gives
# elif (light == "yellow"): #only works if the previous condition is false and this condition is true
#     print("wait")
# else:
#     print("go") #all above conditions are false then this block of code will be executed

#3 grade students based on marks
# marks = int(input("Enter student marks:"))
# if (marks >= 90):
#     print("Grade: A")
# elif (marks >=80 and marks < 90):
#     print("Grade: B")
# elif (marks >= 70 and marks < 80):
#     print("Grade: C")       
# else:
#     print("Grade: D")
    
#4 Nesting
# age = 34

# if (age >= 18):
#     if (age >= 65):
#         print("cannot drive")
#     else:
#         print("can drive")  

#Practice Questions:
#check whether the number entered by the user is odd or even

# num = int(input("Enter a number:"))
# rem = num % 2
# if (rem == 0):
#  print("Even")
# else:
#  print("Odd")   

#find the greatest of 3 numbers entered by the user
# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# c = int(input("Enter third number:"))   
# if(a >= b and a >= c):
#     print("Greatest number is:", a)
# elif(b >= c):
#     print("Greatest number is:", b)
# else:
#     print("Greatest number is:", c)

#if a number is multiple of 7 or not
# x = int(input("Enter a number:"))
# if (x % 7 == 0):
#     print("Multiple of 7")
# else:
#     print("Not a multiple of 7")

