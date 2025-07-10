list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1 = [5, 10, 15, 20, 25, 50, 20]
list1 = [5, 20, 15, 20, 25, 50, 20]

# Extend nested list by adding the sublist
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub_list = ["h", "i", "j"]
# list1[2][1][2].extend(sub_list)
# print(list1)

# Exercise 4: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# var1=[a+b for a in list1 for b in list2]
# print(var1)

# Exercise 6: Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# list2 = list(filter(None,list1))
# print(list2)

# Exercise 7: Add new item to list after a specified item
# a=["Sharvil", 1,2,3,4,5]
# a.append("Name")
# print(a)

# Exercise 3: Turn every item of a list into its square
# b=[5,10,15,20,25]
# c=[]
# for var in b:
#     c.append(var * var)
# print(c)

# Exercise 5: Iterate both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for a,b in zip(list1,list2[::-1]):
    print(a,b)

# Replace list’s item with new value if found
# list1[3]=200
# print(list1)

# list=[2,3,4,5,67]
# print(len(list))

# mylist = {"apple", "banana", "cherry"}
# print(type(mylist))

# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)