# create tuple with one item
# tuple=(1,)
# print(tuple)

# len function
# tuple=(6,7,8,9)
# print(len(tuple))

# type function
# tuple=("my",8,"True",3.4)
# print(type(tuple))

# tuple() constructur
# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)

# access items
# tuple=("my",8,"True",3.4)
# print(tuple[-4:-1])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-6:-1])

# thistuple = ("apple", "banana", "cherry")
# if "kela" in thistuple:
#     print("banana is present in thistuple")
# else:
#     print("kela is not present")

# Unpacking the tuple
# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)

# tropic variable
# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print("green=",green)
# print(tropic)
# print(red)

# Multiply tuple
# fruits = ("apple", "banana", "cherry")
# newtuple=fruits*3
# print(newtuple)

# Sort the tuple
tuple=(9,3,4.2,7)
t2=tuple(sorted(list(tuple), key=lambda x: x[1]))
print(t2)

tuple = ("apple","watermelon", "banana", "cherry")
t2=tuple(sorted(list(tuple), key=lambda x: x[1]))
print(t2)
