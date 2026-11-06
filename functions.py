# def calc_sum(a, b):
#     sum = a+b
#     print(sum)
#     return sum

# calc_sum(2,3)

# Average
# def calc_avg(a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     print(avg)
#     return avg

# calc_avg(1,2,3)

# calculate product
# def cal_prod(a, b): #we can also gve default values here but only from last side
#     print(a*b)
#     return(a*b)

# cal_prod(1,2) #output =2
# cal_prod() #output = error since ntg is passed


# practice questions
# 1. length of a list
# cities = ["delhi", "gurgaon", "noida", "chennai"]
# heroes = ["thpr", "superman", "shaktiman"]

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heroes)

# elements of a list in a single line
# cities = ["delhi", "gurgaon", "noida", "chennai"]
# heroes = ["thpr", "superman", "shaktiman"]
# def print_list(list):
#     for item in list:
#         print(item, end=" ")#|n pushes to next line, but the gap allows the result to appear on the original line

# print_factorial

# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)

# cal_fact(5)
# output: 120

# convert usd to inr
    
# def converter(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val, "USD =", inr_val, "INR")

# converter(7)
# #output: 7 USD = 581 INR

# RECURSION
# 5 to 1 print
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)

# show(5)

# Factorial
# def fact(n):
#     if(n == 0 or n == 1):
#         return 1
#     else:
#         return n * fact(n-1)
#     print

# print(fact(5))

# def calc_sum(n):
#     if(n == 0):
#         return 0
#     return calc_sum(n-1) + n

# sum = calc_sum(5)
# print (sum)


#print all elements in a list
def print_list(list, idx=0):
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["mango", "litchi", "apple", "banana"]
print_list(fruits)
