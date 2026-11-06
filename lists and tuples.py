#Lists[uses square brackets]
# student = ["karan", 95.4, 17, "Delhi"]
# print(student[2])
# student[0] = "Arjun" #lists are mutable, we can change the value of a list
# print(student)

#list slicing
# marks = [90, 80, 70, 60, 50]
# print(marks[1:4])  # Output: [80, 70, 60]
# print(marks[-4:-3])(negative slicing)

#list method
list = [2,1,3]
# print(list)
# list.append(4) #Adds value
# list.sort()#sorts in ascending order
# print(list.sort())#doesn't change the value in itself, so gives null
# print(list) #output=[1,2,3,4]
#list.sort(reverse=True)
# print(list.sort(reverse=True))
# print(list)#output=[4,3,2,1]

# list = ["banana", "a", "e"]
# print(list.sort())
# print(list)
# list.reverse()
# print(list)
# # Output
# #['a', 'banana', 'e']
# # ['e', 'banana', 'a']
# list.insert(1,5) #1 is the moemory address and 5 is the value added
# print(list) #output = ['e', 5, 'banana', 'a']

#removing iterms from list
# list = [2,1,3,1]
# list.remove(1)#removes the first occurence of 1 from the memory location
# list.pop(2)#removes the value stored inside the 2nd storage location
# print(list)
 
 #tuples(immutable just like strings)[uses straight brackets]
# mew= (2,1,3,1)
# print(type(mew))#output class 'tuple'
# print(mew[0])
# print(mew[1])
# mew[0] = 5 #value can't be added or assigned or changed like lists

# mew = () #its accepted as a tuple
# print(type(mew))
# print(mew)

# mew = (2,) #always use comma to separate to create a tuple or it could be interpreted as a different-
# #-data type just like mew2 = (2) was interpreted as an integer data type)
# mew2 = (2)
# print(type(mew))
# print(type(mew2))
# print(mew)
# print(mew2)

#tuples slicing
# tup = (2,1,3,1)
# print(tup.index(3)) #1 is the value and the answer will be 2, showing the memory location
# print(tup.count(1)) #total number of times the value 1 is repeated will be shown 
# #Output
# 2
# 2

#Practice questions
#enter name of 3 fav movies, store them in a list
# movies = []
# movies.append(input("enter 1st movie:"))
# movies.append(input("enter 2nd movie:"))
# movies.append(input("enter 3rd movie"))
# print(movies)

# movies = []
# mov1 = input("Enter 1st movie")
# mov2 = input("Enter 2nd movie")
# mov3 = input("Enter 3rd movie")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

#Palindrome
# list1 = [1,2,1]
# list2 = [3,2,1]
# copylist1 = list1.copy() #returns a shallow cpy of a list
# copylist1.reverse()
 
# if(copylist1 == list1):
#     print("palindrome")
# else:
#     print("Not palindrome")    

#count the no of students with A grade and store the above values in a list 
grade = ("C", "D", "A", "A", "A", "B", "A")
print(grade.count("A"))
print(grade)

