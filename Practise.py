# tuple=(1,2,3,4,5)
# print(tuple[::-1])


# tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
# t2=tuple(sorted(list(tuple1),key=lambda x:x[1]))
# print(t2)

# Copy specific elements from one tuple to a new tuple
# tuple1 = (11, 22, 33, 44, 55, 66)
# tuple2=tuple1[2:5]
# print(tuple2)

# Counts the number of occurrences of item 50 from a tuple
# tuple1 = (50, 50, 50, 50, 50,100,200,300)
# print(tuple1.count(200))

# Rename key of a dictionary
# D1={"Name":"Sonali","number":11,"Flatno":908,"name":"Sharvi"}
# print(D1.update["Name":"name"])

# Convert two lists into a dictionary
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dict1=dict(zip(keys,values))
# print(dict1)

# Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict3={**dict1,**dict2}
# print(dict3)

# Print the value of key ‘history’ from the below dict
# SampleDict = {
#      "class": {
#          "student": {
#              "name": "Mike",
#              "marks": {
#                  "physics": 70,
#                  "history": 80
#              }
#          }
#      }
#  }
# print(SampleDict["class"]["student"]["marks"]["history"])

# Initialize dictionary with default values
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# dict1=dict.fromkeys(employees,defaults)
# print(dict1)

# Delete a list of keys from a dictionary
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# # Keys to remove
# keys=["name","salary"]
# for a in keys:
#     sample_dict.pop(a)
#     print(sample_dict)

# Check if a value exists in a dictionary
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# if 200 in sample_dict.values():
#     print("Value is exist")
# else:
#     print("Value is not exists")

# Rename key of a dictionary
# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
# sample_dict["Location"]=sample_dict.pop("city")
# print(sample_dict)

# Get the key of a minimum value from the following dictionary
# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# print(max(sample_dict,key=sample_dict.get))

# Change value of a key in a nested dictionary
# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }
# sample_dict["emp1"]["salary"]=8500
# print(sample_dict)

# Create a dictionary by extracting the keys from a given dictionary
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
# keys = ["name", "salary"]
# sample_dict

# print 1 to 25 numbers in reverse order.
# count=25
# while count>=1:
#     print(count)
#     count-=1

# Add a method called welcome to the Student class:
# class Student:
#     def devision(self):
#         print("A")

#     def welcome(self):
#         print("Welcome to the A devision")
# obj=Student()
# obj.devision()
# obj.welcome()

# print((6 + 3) - (6 + 3))

# print(5 + 4 - 7 + 3)


# num=123
# reverse=int(str(num)[::-1])
# if num==reverse:
#     print("Number is palindrome")
# else:
#     print("Number is not palindrome")

# num=13
# reverse=int(str(num)[::-1])
# if num==reverse:
#     print("Number is Palindrome")
# else:
#     print("Number is not Palindrome")

# print first 10 natural numbers
# count=1
# while count<=10:
#     print(count)
#     count+=1

# print 50 to 60 natural numbers
# num=50
# while num<=60:
#     print(num)
#     num+=1

# print 1 to 25 reverse numbers
# count=25
# while count>=1:
#     print(count)
#     count-=1

# Interchange first and last elements in a list
# list=[4,5,2,7,9,10]
# list[0],list[-1]=list[-1],list[0]
# print("List after swapping:",list)

# Swap two elements in a list
# list=[10,20]
# # list[0],list[1]=list[1],list[0]
# # print(list)

# x,y=[10,20]
# x,y=y,x
# print("x=",x)
# print("y=",y)

# len of list
# list=[10,20]
# print(len(list))

# string palindrome
# s="malayalam"
# if s==s[::-1]:
#     print("String is palindrome")
# else:
#     print("String is not palindrome")

# print the pattern
# 1
# 1,2
# 1,2,3
# 1,2,3,4
# 1,2,3,4,5
# row=5
# for i in range(1,row+1,1):
#     for j in range(1,i+1):
#         print(j, end='')
#     print()

# Sum of all numbers from 1 to given list
# num=int(input("Enter munber"))
# var=sum(range(1,num+1))
# print(var)

# print multiplication table of given number
# num=int(input("Enter number"))
# for i in range(1,11,1):
#     table=num*i
#     print(table)

# print full multiplication table
# n=int(input("Enter number"))
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j, end='')
#     print()

# add 2 numbers in python
# num1=10
# num2=10
# print(num1+num2)

# n1=int(input("Enter first number"))
# n2=int(input("Enter second number"))
# n3=n1+n2
# print(n3)

# max, min number in python
# num1=15
# num2=20
# # print(min(15,20))
# if num1>num2:
#     print("num1 is greater")
# elif num2>num1:
#     print("num2 is grater")

# Factorial of a given number
# fact=6
# while fact<=6:
#     print(fact)
#     fact*=1

# n=6
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

# Python program for simple interest
# def fun(p,t,r):
#     return (p*t*r)/100
# res=fun(8,6,8)
# print(res)

# interest=lambda p,t,r:(p*t*r)/100
# print(interest(8,6,8))

# Exercise 3: Create a tuple with single item 50
# tuple=(2,)
# print(tuple)

# Reverse the tuple
# tuple=(1,2,3,4,5)
# print(tuple[::-1])

# Access value 20 from the tuple
# tuple=(1,2,[3,4],5)
# tuple[1][1]= 6
# print(tuple)
# tuple1 = (11, [22, 33], 44, 55)
# tuple1[1][0]=222
# print(tuple1)

# Exercise 4: Unpack the tuple into 4 variables
# tuple=(1,2,3,4)
# w,x,y,z=tuple
# print("w=",w)
# print("x=",x)
# print("y=",y)
# print("z=",z)

# Exercise 5: Swap two tuples in Python
# tuple1=(1,2,3,4)
# tuple2=(5,6,7,8)
# tuple1,tuple2=tuple2,tuple1
# print("tuple1=",tuple1)
# print("tuple2=",tuple2)

# Exercise 6: Copy specific elements from one tuple to a new tuple
# tuple=(1,2,3,4,5.6)
# tuple1=tuple[2:5]
# print(tuple1)

# Exercise 8: Sort a tuple of tuples by 2nd item
# tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
# tuple2=tuple(sorted(list(tuple1),key=lambda x:x[1]))
# print(tuple2)

# Exercise 9: Counts the number of occurrences of item 50 from a tuple
# tuple1 = (50, 10, 50, 70, 50)
# print(tuple1.count(50))

# Exercise 1: Convert two lists into a dictionary
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dict1=dict(zip(keys,values))
# print(dict1)

# Exercise 2: Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict3={**dict1,**dict2}
# print(dict3)

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2=dict1.values()
# print(dict2)

# Exercise 3: Print the value of key ‘history’ from the below dict
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# print(sampleDict['class']['student']['marks']['history'])

# Exercise 7: Check if a value exists in a dictionary
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# if 200 in sample_dict.values():
#     print("200 value is Present")

# if 200 in sample_dict.values():
#     print("200 value is present")

#  Change value of a key in a nested dictionary
# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }
# dict=sample_dict['emp3']['salary']=8500
# print(dict)

# Get the key of a minimum value from the following dictionary
# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# print(min(sample_dict,key=sample_dict.get))

# Exercise 8: Rename key of a dictionary
# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
# sample_dict['location']=sample_dict.pop('city')
# print(sample_dict)

# Delete a list of keys from a dictionary
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# # Keys to remove
# keys = ["name", "salary"]
# for a in keys:
#     sample_dict.pop(a)
# print(sample_dict)

# Initialize dictionary with default values
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# dict1=dict.fromkeys(employees,defaults)
# print(dict1)

## Initialize dictionary with default values
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# dict1= dict.fromkeys(employees,defaults)
# print(dict1)

# Exercise 1: Reverse a list in Python
# list=[1,2,3,4]
# # print(len(list))
# print(list[::-1])

# Exercise 2: Concatenate two lists index-wise
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# print(list1[0]+list2[0],list1[0]+list2[1]])
# print(list1+list2)



# Print first 10 natural numbers using while loop
# count=25
# while count>=1:
#     print(count)
#     count-=1

# Exercise 2: Print the following pattern
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

# row=5
# for i in range(1,row+1,1):
#     for j in range(1,i+1):
#         print(j, end='')
#     print("")

# Calculate sum of all numbers from 1 to a given number
# num=int(input("Enter a number"))
# var=sum(range(1,num+1))
# print(var)


# Print multiplication table of a given number
# num=int(input("Enter number"))
# for i in range(1,11,1):
#     multi=num*i
#     print(multi)

# Print Full Multiplication Table
# 

a=["Sharvil", 1,2,3,4,5]
b=[5,10,15,20,25]
print(a+b)





 



