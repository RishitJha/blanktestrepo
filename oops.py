# class Student:
#     name = "Rishit"
# s1 = Student()
# print(s1)
# print(s1.name)


#_init_ function
# class Student:
#     def __init__(self, fullname): #It is automatically invoked but can alse be declared(self always needs to be called ig, while fullname is the variable that makes things work)
#         self.name = fullname
#         print("adding new student tot database..")

# s1 = Student("Karan")
# print(s1.name) #Karan

# class Student:
#     #default constructors:
#     def __init__(self):
#         pass

#     #parameterized consturctors:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student to database")

# s1 = Student("Karan", 97)
# print(s1.name, s1.marks)#karan, 97

# s2 = Student("arjun", 98)
# print(s2.name, s2.marks)#arjun, 98

#Output
# adding new student to database
# Karan 97
# adding new student to database
# arjun 98

# Attribute
# class Student:
#     college_name = "ABC College" #class attr
#     #parameterized consturctors:
#     def __init__(self, name, marks):
#         self.name = name #obj.attr can be accessed using .name
#         self.marks = marks
#         print("adding new student to database")

# s1 = Student("Karan", 97)
# print(s1.name, s1.marks)#karan, 97

# s2 = Student("arjun", 98)
# print(s2.name, s2.marks)#arjun, 98

# print(Student.college_name)

# adding new student to database
# Karan 97
# adding new student to database
# arjun 98
# ABC College

# Classes can store both data(attributes) and methods(functions made for objects)

# class Student:
#     college_name = "ABC College" #class attr
#     #parameterized consturctors:
#     def __init__(self, name, marks):
#         self.name = name #obj.attr can be accessed using .name
#         self.marks = marks
#         print("adding new student to database")

#     def welcome(self):
#         print("Welcome student", self.name)

#     def getmarks(self):
#         return self.marks
    
# s1 = Student("Karan", 97)
# s1.welcome()
# print(s1.getmarks())


#Practice QuESTINS
#sTUDENT CLASS THAT TAKES NAME AND MARKS OF 3 SUBJECTS AS ARGUMENTS  IN CONSTRUCTOR
#METHOF TO PRINT THE AVERAGE
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name, "you avg score is:")

# s1 = Student("tony stark", [99, 98, 97])
# s1.get_avg()
#  #change the attribute name
# s1.name = "ironman"
# s1.get_avg()

#static methods
#methods that don't use the self parameter(work at class level)
# class Student:
#     @staticmethod #decorator
#     def college():
#         print("ABC College")

#Important concepts:
#Abstraction:
#Hiding the implementation details of a class and only showing the essential features of the user
#Encapsulation
#wrapping data and funtions into a single unit(object

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car started....")

# car1 = Car()
# car1.start()

#Practice Questions:
# Account with 2 attributes-balance and account no:
# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc

# #Debit Method
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited")
#         print("total balance =", self.get_balance)

#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was credited")
#         print("total balance =", self.get_balance)
#     def get_balance(self):
#         return self.balance

# acc1 = Account(10000, 12453)
# print(acc1.balance)
# print(acc1.account_no)
# acc1.debit(1000)
# acc1.credit(500)
