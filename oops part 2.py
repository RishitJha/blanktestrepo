# # #delete keyword
# # # class student:
# # #     def __init__(self, name):
# # #         self.name = name

# # # s1 = student("shraddha")
# # # print(s1.name)
# # # del s1.name
# # # print(s1.name)

# # #private like attributes and methods
# # #to be used only within the class and not accessible from outside the class

# # # class Account:
# # #     def __init__(self, acc_no, acc_pass):
# # #         self.acc_no = acc_no
# # #         self.acc_pass = acc_pass #to make an attribute private just add two underscores
# # #         self.__acc_pass = acc_pass #to make an attribute private just add two underscores
# # # acc1 = Account("12345","abcde")

# # # print(acc1.acc_no)
# # # print(acc1.acc_pass)

# # # class Account:
# # #     def __init__(self, acc_no, acc_pass):
# # #         self.acc_no = acc_no
# # #         self.acc_pass = acc_pass #code is passed to the object
# # #         self.__acc_pass = acc_pass#code isn't passed to the object and stays hidden within the class(use __)
    
# # #     def reset_pass(self):
# # #         print(self.__acc_pass)
# # # acc1 = Account("12345", "abcde")
# # # print(acc1.acc_no)
# # # print(acc1.acc_pass)#acc password will be shown 
# # # # print(acc1.__acc_pass)#acc password will not be shown 
# # # print(acc1.reset_pass())

# # #output
# # # 12345
# # # abcde
# # # abcde
# # # None

# # # class Person:
# # #     __name = "anonymous"

# # #     def __hello(self):
# # #         print("hello person")

# # #     def welcome(self):
# # #         self.__hello()

# # # p1 = Person()
# # # print(p1.__hello())

# # #Output:
# # #   File "c:\Users\jrish\blanktestrepo\oops part 2.py", line 54, in <module>
# # #     print(p1.__hello())(error is shown  because they are privatized withthe underscores)
# # #           ^^^^^^^^^^
# # # AttributeError: 'Person' object has no attribute '__hello'
# # # 
# # # class Person:
# # #     __name = "anonymous"

# # #     def __hello(self):
# # #         print("hello person")

# # #     def welcome(self):
# # #         self.__hello()

# # # p1 = Person()
# # # print(p1.welcome())

# # #Output:
# # # hello person(the private attribute __hello is accessed within the class)
# # #None   

# # #Inheritance
# # #One class derives the properties and methods of another class
# # # class Car:
# # #     ....

# # # class ToyotaCar(Car):
# # #     ....

# # class Car:
# #     @staticmethod
# #     def start():
# #         print("car started....")

# #     @staticmethod
# #     def start():
# #         print("car stopped....")

# # class ToyotaCar(Car):
# #     def __init__(self, name):
# #         self.name = name

# # car1 = ToyotaCar("Fortuner")
# # car2 = ToyotaCar("Prius")

# # print(car1.start()) #The code derives its work from the Car class

# #Types of inheritance 
# #Single inheritance(single base class and single child class as seen as above)
# #Multi-level Inhertiance(Single base class, child class derives its features from the base class and the single child class attributes are inherited by another class)

# # class Car:
# #     @staticmethod
# #     def start():
# #         print("car started....")

# #     @staticmethod
# #     def stop():
# #         print("car stopped....")

# # class ToyotaCar(Car):
# #     def __init__(self, brand):
# #         self.name = brand

# # class Fortuner(ToyotaCar):
# #     def __init__(self, type):
# #         self.type = type

# # car1 = Fortuner("diesel")
# # car1.start()

# #Output
# # car started....Fortuner derives it from toyotacar and then toyotacar derives itself from car class

# #Multiple Inheritance:
# #Derives it properties from multiple base classes

# # class A:
# #     varA = "Welcome to class A"

# # class B:
# #     varB = "Welcome to class B"

# # class C(A, B): #Here the bracket allows the inheritance
# #     varC = "Welcome to class C"

# # c1 = C()

# # print(c1.varC)
# # print(c1.varB)
# # print(c1.varA)
# #oUTPUT
# # Welcome to class C
# # Welcome to class B
# # Welcome to class A



# #Super Method

# # class Car:
# #     def __init__(self, type):
# #         self.type = type

# #     @staticmethod
# #     def start():
# #         print("car started...")
# #     @staticmethod
# #     def stop():
# #         print("car started...")

# # class ToyotaCar(Car):
# #     def __init__(self, name, type): #The definition is collected from the main class and then passed on)
# #         self.name = name
# #         super().__init__(type) The super method is used to call method of the parent class

# # car1 = ToyotaCar("prius","electric")
# # print(car1.type)

# # Class Method
# #Static method is bound to the class and receives the class as an implicit first argument
# #it can;t access or modify class state and generally for utility

# # class Person:
# #     name = "Anonymous"

# #     @classmethod
# #     def changeName(cls, name): #Not referrring to self but rather to class
# #         cls.name = name

# # p1 = Person()
# # p1.changeName("rahul kumar")
# # print(p1.name)
# # print(Person.name)

# #Output
# # rahul kumar
# # rahul kumar

# # Property:
# # class Student:
# #     def __init__(self, phy, chem, math):
# #         self.phy = phy
# #         self.chem = chem
# #         self.math = math
# #         self.percentage = str((self.phy + self.chem + self.math)/3) + "%"  

# # stu1 = Student(98, 97, 99)
# # print(stu1.percentage)

# # stu1.phy = 86
# # print(stu1.phy)
# # # stu1.calcPercentage()
# # print(stu1.percentage)

# #Output:
# # 98.0%
# # 86
# # 98.0%
# #Reasoning: The code gives the same percentage despite the change in marks due to the old value of percentage still registered as same


# # class Student:
# #     def __init__(self, phy, chem, math):
# #         self.phy = phy
# #         self.chem = chem
# #         self.math = math
# #         self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

# #     def calcPercentage(self):
# #         self.percentage = str((self.phy + self.chem + self.math)/3) + "%"
       

# # stu1 = Student(98, 97, 99)
# # print(stu1.percentage)

# # stu1.phy = 86
# # print(stu1.phy)
# # stu1.calcPercentage()
# # print(stu1.percentage)

# #Output:
# # 98.0%
# # 86
# # 94.0%

# #Reasoning: The code gives diff value after the marks changed because the method or function(calcpercentage) was called before calculating the percentage:
# #Property: The following code uses property which allows the percentage to be formed and any change in the marks variable results change in the percentage)
# # class Student:
# #     def __init__(self, phy, chem, math):
# #         self.phy = phy
# #         self.chem = chem
# #         self.math = math
        
# #     @property
# #     def percentage(self):
# #         return str((self.phy + self.chem + self.math)/3) + "%"

# # stu1 = Student(98, 97, 99)
# # print(stu1.percentage)

# # stu1.phy = 86
# # print(stu1.percentage)

# #Output:
# #98.0%
# #94.0%(the value is)

# #Polymorphism: Operator Overloading
# #same operator is allowed to have differnt meanings

# #Polymorphism
# #Same operator is allowed to have different meanings

# #Operator and Dunder functions
# # print(1 + 2) #3
# # print("apna" + "college") #concatenate
# # print([1,2,3] + [4,5,6]) #merge

# #Output
# # 3
# # apnacollege
# # [1, 2, 3, 4, 5, 6]

# # class Complex:
# #     def __init__(self, real, img):
# #         self.real = real
# #         self.img = img

# #     def showNumber(self):
# #         print(self.real,"i +",self.img,"j")

# #     def add(self, num2):
# #         newReal = self.real + num2.real
# #         newImg = self.img + num2.img
# #         return Complex(newReal, newImg)
# # num1 = Complex(1,3)
# # num1.showNumber()


# # num2 = Complex(4,6)
# # num2.showNumber()

# # num3 = num1.add(num2)
# # num3.showNumber()

# # print(num1 + num2) #will gie error, because complex numbers can't be operated on inpython without functions or using dunder functions
# # #Output
# # # 1 i + 3 j
# # # 4 i + 6 j
# # # 5 i + 9 j


# # class Complex:
# #     def __init__(self, real, img):
# #         self.real = real
# #         self.img = img

# #     def showNumber(self):
# #         print(self.real,"i +",self.img,"j")

# #     def __add__(self, num2): #usage of dunder functions allowed the work of imaginary numbers addition to happen
# #         newReal = self.real + num2.real
# #         newImg = self.img + num2.img
# #         return Complex(newReal, newImg)
# # num1 = Complex(1,3)
# # num1.showNumber()


# # num2 = Complex(4,6)
# # num2.showNumber()

# # num3 = num1 + num2
# # num3.showNumber()

# # #Output
# # 1 i + 3 j
# # 4 i + 6 j
# # 5 i + 9 j


# # class Complex:
# #     def __init__(self, real, img):
# #         self.real = real
# #         self.img = img

# #     def showNumber(self):
# #         print(self.real,"i +",self.img,"j")

# #     def __sub__(self, num2): #usage of dunder functions allowed the work of imaginary numbers addition to happen
# #         newReal = self.real - num2.real
# #         newImg = self.img - num2.img
# #         return Complex(newReal, newImg)
# # num1 = Complex(1,3)
# # num1.showNumber()


# # num2 = Complex(4,6)
# # num2.showNumber()

# # num3 = num1 - num2
# # num3.showNumber()
#  #output
# #  1 i + 3 j
# # 4 i + 6 j
# # -3 i + -3 j

# #Practice Questions:
# #define a circle to create a circle with radius r using the constructor
# #define an area() method of the class which calculates the area of the circle
# #define a perimeter() method of the class which allow to calculate the perimeter of the circle:


# class Circle:
#     def __init__(self, radius):#Constructor
#         self.radius = radius 

#     def area(self): #Method 
#         return 3.14 * self.radius ** 2

#     def perimeter(self): #Method
#         return 2*3.14*self.radius
    
# c1 = Circle(21)  
# print(c1.area())
# print(c1.perimeter())

# #Output:
# 1384.74
# 131.88

#An employee class with attributes role, department and salary. The class alsp has a showDetails() method.
#An engineer class that inherits properties from employee and has additional attributes: name and age
# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("role =", self.role)
#         print("dept =", self.dept)
#         print("salary =", self.salary)

# class Engineer(Employee):
#     def __init__(self, name, age):
#          self.name = name
#          self.age = age
#          super().__init__("Engineer","IT","75000")


# engg1 = Engineer("Elon Musk", 40)
# engg1.showDetails()

# #Result:
# role = Engineer
# dept = IT
# salary = 75000


#create a class called order which stores item and its price 
#Use dunder function__gt__() to convey that:
#order1>order2 if price of order1>price of order 2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price


odr1 = Order("chips", 20)
odr2 = Order("tea", 25)

print(odr1 > odr2)
#Output
False