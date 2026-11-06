# # while Loop
# i=5
# while i<6:
#     print(i)
#     i -= 1

# print("Loop ended") #an example of negative loop always avoid such loops creation

#Practice questions
#Numbers from 1 to 100
# i=1
# while i<=100:
#     print ("the number is:", i)
#     i += 1

# #Numbers from 100 to 1
# i=100
# while i >= 1:
#     print(i)
#     i -= 1
#Multiplication table of a number n
# n=int(input("Enter a number"))
# i=1
# while i<=10:
#     print ("the product is:", n*i)
#     i += 1

#Print the elements of the following list:
#[1,4,9,16,25,36,49,64,81,100]
# nums=[1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx += 1



#Search for a number x in this tuple using loop:
# nums = (1,4,9,16,25,36,49,64,81,100)
# x = 36
# i = 0
# while i < len(nums):
#     if(nums[i] == x):
#         print("Found at idx", i)
#     else:
#         print("finding:")
#     i += 1


# #BREAK STATEMENT
# i = 1
# while i <= 5:
#     print(i)
#     if(i==3):
#         break
#     i += 1

# #Search for a number x in this tuple using loop:
# nums = (1,4,9,16,25,36,49,64,81,100)
# x = 36
# i = 0
# while i < len(nums):
#     if(nums[i] == x):
#         print("Found at idx", i)
#         break 
#     else:
#         print("finding:")
#     i += 1

#CONTINUE : Terminates the current line and continues th next one again
# i = 0
# while i <= 5:
#     if (i==3):
#         i += 1
#         continue
#     print(i)
#     i += 1


# #FOR LOOP(LOOPS FOR SEQUENTIAL TRAVERSAL, LISTS, STRINGS, TUPLES
# list = [1,2,3,4,5]
# for val in list:
#     print(val)


# my_string = "apnacollege"
# for char in my_string:
#     if (char == 'o'):
#         print("o found")
#         break
#     print(char)
# else:
#     print("END") #THE BREAK statement caused this line to be exitted and hence only the following end command was printed
# print("END")

#ELment of list, print them using loop
# to_be_printed = [1,4,9,16,25,36,49,64,81,100]
# for el in to_be_printed:
#     print(el)

#Search for a number x in the tuple using loop
#linear search

# nums = (1,4,9,16,25,36,49,64,81,100,49)
# x = 49
# idx = 0
# for el in nums:
#     if (el == x):
#         print("number found at idx",idx)
#         break
#     idx += 1

#Range
# three ways to write:
# range(start?, stop, step?)

# for el in range(5): #range(stop)
#     print(el)

# for el in range(1,5): #range(start, stop)
#     print(el)

# for el in range(1,5,2): #range(start, stop, step)
#     print(el)   

# for i in range(100,1,-1):
#     print(i)

# n = int(input("Enter number:"))
# for i in range(1,11):
#     print(n*i)


#PASS STTATEMent(for future code leaves a space)
#Practice question
#sum of first n natural numbers(using while)
# n = 5
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# for i in range(1, n+1):
#     sum += i
# print("total sum = ", sum)

#factorial of first n numbers
n = 4
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("factorial =", fact)