# f = open("lets see.txt", "r")
# data = f.read()
# #data = f.read(5)#output the first 5characters
# line1 = f.readline()
# print(line1)
# print(data)
# print(type(data))
# f.close()

# f = open("lets see.txt", "w")

# f.write("I want to learn jv tomorrow, 123")

# f.close()

# f = open("lets see.txt", "a")

# f.write("I want to learn jv tomorrow, 123")

# f.close()

# Practice Questions:
# Wtrite into a file, the following info, in different line:
# with open("pratice.txt","w") as f:
#     f.write("Hi everyone\n we are learning File I/O\n")
#     f.write("using Java.\n I like programming in java")


#replace all occurences of Java with Python in above file:
# with open("pratice.txt","r") as f:
#     data = f.read()

# new_data = data.replace("Java", "Python")
# print(new_data)

# with open("pratice.txt", "w") as f:
#     f.write(new_data)

#find the word learning
# word ="learning"
# with open("pratice.txt", "r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("found")
#     else:
#         print("not found")

#which line of the file does the word "learning"first occur?
# def check_for_line():
#     word ="learning"
#     data = True
#     line_no = 1
#     with open("pratice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return 
#             line_no += 1

#     return -1
# check_for_line()

#From a file containing numbers separated by comma, print the count of even number:
# with open("pratice.txt", "r") as f:
#     data = f.read()
#     print(data) 

#     num = ""
#     for i in range(len(data)):
#         if (data[i] == ","):
#             print(num)
#             num = ""
#         else:
#             num += data[i]

# count = 0
# with open("pratice.txt", "r") as f:
#     data = f.read()

#     nums = data.split(",")
#     for val in nums:
#         if(int(val) % 2 == 0):
#             count += 1

#     print(count)

    