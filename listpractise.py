# change the list item
# list=["Apple","banana","cheery"]
# list[1]="peru"
# print(list)

# change range of item values
# list=["Apple","banana","cheery"]
# list[1:2]=["peru","mango"]
# print(list)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# list constructur
# thislist=list(("apple","banana","cheery"))
# print(thislist)

# len function & type method
# list=[1,2,3,4]
# print(len(list))
# print(type(list))

# Negative indexes
# list=[1,2,3,4]
# print(list[-3:-1])

# check if item is exist in a list
# list=[1,2,3,4]
# if 5 in list:
#     print("Item found") 
# else:
#     print("item not found")

# Insert new item
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)
# print(thislist[0])

# mylist = ['apple', 'banana', 'cherry']
# mylist.insert(1,"Papai")
# print(mylist)

# append method
# mylist = ['apple', 'banana', 'cherry']
# mylist.append("watermelon")
# print(mylist)

# extend method
# list1=[1,2,3,4]
# list2=[5,6,7,8]
# list1.extend(list2)
# print(list1)

# extend tuple to list
# list1=[1,2,3,4]
# tuple1=(5,6,7,8)
# list1.extend(tuple1)
# print(list1)

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# remove() item from list
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("apple")
# print(thislist)

# del keyword
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)
# del thislist

# thislist = ["apple", "banana", "cherry"]
# del thislist

# pop method
# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)

# clear method
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# # loop through list
# thislist = ["apple", "banana", "cherry"]
# for i in thislist:
#     print(i)

# list comphrension
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)

# sort method
# list=[6,7,2,8,9,10]
# list.sort()
# print(list)

# sort in decending order
# list=[6,7,2,8,9,10]
# list.sort(reverse=True)
# print(list)

# reverse method
# list=[6,7,2,8,9,10]
# list.reverse()
# print(list)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

# copy list
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# list=thislist.copy()
# print(list)

# list method to copy the list
# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

# slice operator
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist[:]
# print(mylist)

# join 2 lists
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3=list1 + list2
# print(list3)

# join 2 lists with append method
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# for x in list2:
#     list1.append(x)
# print(list1)


# join 2 lists with extend method
# 

# Exercise 1: Reverse a list in Python
# list2 = [1, 2, 3]
# # list2.reverse()
# print(list2[::-1])

# Exercise 2: Concatenate two lists index-wise
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# print(list1+list2)

# Exercise 4: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# var=[a+b for a in list1 for b in list2]
# print(var)

# Exercise 3: Turn every item of a list into its square
# b=[5,10,15,20,25]
# c=[]
# for var in b:
#     c.append(var*var)
# print(c)

# Exercise 5: Iterate both lists simultaneously
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# for a,b in zip(list1,list2[::-1]):
#     print(a,b)

# Exercise 6: Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# list2=list(filter(None,list1))
# print(list2)

# Exercise 7: Add new item to list after a specified item
# list1 = [5, 10, 15, 20, 25, 50, 20]
# list1.append("Sona")
# print(list1)
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# # Expected output:
# # sublist=[2000]
# # [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)

# Exercise 8: Extend nested list by adding the sublist
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# # sub list to add
# sub_list = ["h", "i", "j"]
# list1[2][1][2].extend(sub_list)
# print(list1)

# Exercise 9: Replace list’s item with new value if found
# list1 = [5, 20, 15, 20, 25, 50, 20]
# list1[1]=200
# print(list1)

# Exercise 10: Remove all occurrences of a specific item from a list.
list1 = [5, 20, 15, 20, 25, 50, 20]
# for var in list1:
#     if 20 in list1: 
#         list1.remove(var)
#         print(list1)
list1.count(20)
print(list1)