# # #dictionary used in python to store data values in key:value pairs
# # #unordered, mutable and don't allow duplicate keys
# # info = {
# #     "key" : "value", #key can also be tuples, integrers and strings
# #     "name" : "apnacollege",
# #     "learning" : "coding",
# #     "age": 35,
# #     "is_adult" : True,
# #     "marks" : 94.4
# # }
# # print(type(info))
# # info["name"] = "rishitjha"
# # # print(info) (no index exists so unordered, mutable and duplicate keys aren't allowed)
# # print(info["name"]) #to print the data inside variables use this command since there is no formal memory location allocated
# # print(info) #the values in the name section is changed

# #Nested Dictionaries
# student = {
#     "name" : "rishitjha",
#     "subjects" :{
#         "phy" : 98,
#         "chem" : 95,
#         "math" : 67
#     }
# }
# print(student) #prints all the data in the dictinary
# print(student ["subjects"]["chem"]) #prints the data in the memory location within the dictionary


# #other commands and keywords
# print(student.keys()) #prints the outer keys, not the subkeys
# print(list(student.keys())) #prints the same above data, just converts the data type to list
# print(student.values()) #prints the values within the keys
# print(student.items()) #prints the values in key and pairs
# print(student["name"]) #prints the name value
# # print(student.get["name"]) #prints the name too
# # # print(student["name2"]) #error is shown 
# # print(student.get("name2"))#no error prints only none as output 

# student.update ({"city":"delhi", "age":16}) #adds extra data to the old dictionary
# print(student) 

# #Sets
# #sets are mutable but its elements aren't
# # Collection of the unordered iterms, and each element in the set must be unique and immutable
# #can't store lists and dictonaries inside it cause they are mutable
# collection = {1,2,2,3,"hello", "world", "world"}
# print(collection)
# print(len(collection)) #toal no of items
# #output = no data or value will be repeated
#  #to create an empty set
#  collection = set() #empty set;syntax to convert it to set data type since {} alone would indicate dictionary data type

# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add("apna college")
# collection.add((1,2,3))
# print(collection)
# collection.remove(2)
# print(collection)
# print(len(collection))
# collection.clear()
# print(len(collection))
# #utput
# # 1, 2, 'apna college', (1, 2, 3)}
# # {1, 'apna college', (1, 2, 3)}
# # 3
# # 0

# set1 = {1,2,3}
# set2 = {2,3,4}
# print(set1.union(set2)) #(1,2,3,4)
# print(set1.intersection(set2)) #(2,3)

#practice questions
#store following and meaning in a python dictonary:
dictionary = {
    "cat" : "a small animal",
    "table" : ["furniture", "list of figures"]
}
print(dictionary)
#output
{'cat': 'a small animal', 'table': ['furniture', 'list of figures']}

#assume given a list of subjects for students, assumre one classroom is reqd for 1 subejct, how many classrooms are needed by all subjects
subjects = {
    "a","b", "c", "d", "e"    
}
print(len(subjects))

#enter marks of 3 subjects from the user and store them in a dictionary, start with an empty dicotinary and add one by one, use subject name as key and marks as value
marks = {}
x = int(input("enter phy:"))
marks.update({"phy" : x})

x = int(input("enter math:"))
marks.update({"maths" : x})

x = int(input("enter bio:"))
marks.update({"bio" : x})

print(marks)