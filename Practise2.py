# print 1 to 25 numbers in reverse order.
# count=25
# while count>=1:
#     print(count)
#     count-=1

# Print first 10 natural numbers using while loop
# a=1
# while a<=10:
#     print(a)
#     a+=1

# print the patter
# 1
# 1,2
# 1,2,3
# 1,2,3,4
# 1,2,3,4,5
# row=5
# for i in range(1,row+1,1):
#     for j in range(i,i+1):
#         print(j, end='')
#     print("")

# row=5
# for i in range(1,row+1,1):
#     for j in range(1,i+1):
#          print(j, end='')
#     print("")

# Calculate sum of all numbers from 1 to a given number
# number=int(input("Enter a number"))
# var=sum(range(1,number+1))
# print(var)

# Print multiplication table of a given number
# n=int(input("Enetr number"))
# for i in range(1,11,1):
#     table=n*i
#     print(table)

# Display numbers from a list using a loop
# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     print(i)

# Print Full Multiplication Table
# n=int(input("Enter Number"))
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j, end='')
#     print()

# x="sonali"
# print(x)

# day = 4
# match day:
#   case 1:
#     print("Monday")
#   case 2:
#     print("Tuesday")
#   case 3:
#     print("Wednesday")
#   case 4:
#     print("Thursday")
#   case 5:
#     print("Friday")
#   case 6:
#     print("Saturday")
#   case 7:
#     print("Sunday")

# class Animal:
#     def speak(self):
#         pass
# class Dog:
#     def speak(self):
#         print("Bho Bho")
# dog=Dog()
# dog.speak()

# a = 4
# x = "Sally"
# print(x)
# #A will not overwrite a

# x = 4       # x is of type int
# x = "Sally" # x is now of type str
# print(x)

# x=y=z="orange"
# print(x)
# print(y)
# print(z)

# # unpack list
# fruits=["apple","baanana","Chikko"]
# x,y,z=fruits
# print("x=",x)
# print("y=",y)
# print("z=",z)

# x='my '
# y='name '
# z=5
# print(x,y,z)

# myvar="sonali"
# def mystring():
#     myvar="sharvi"
#     print(myvar)
# mystring()
# print(myvar)

# x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)

# global keyword
# def myfun():
#     global x
#     x='sonali'
#     print(x)
# myfun()
# # print(x)

# a = "Hello, World!"
# print(a[1])

# txt = """The best things in life are free!"""
# print(txt)

# b = "Hello, World!"
# print(b[2:5])

# b = "Hello, World!"
# print(b[:5])

# b = "Hello, World!"
# print(b[2:])

# b = "Hello, World!"
# print(b[-5:-2])

# a = "Hello, World!"
# print(a.replace("H", "J"))

# age=30
# txt=f"My name is sonali and Age is {age}"
# print(txt)

# price = 59
# txt = f"The price is {price} dollars"
# print(txt)

# txt = f"The price is {20 * 59} dollars"
# print(txt)

# txt = "PeoPLES"
# print(txt.encode())

# a = 200
# b = 33

# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")

# print(bool("Hello"))
# print(bool(15))

# x = "Hello"
# y = 15

# print(bool(x))
# print(bool(y))

# def myFunction() :
#   return True

# print(myFunction())

num=122
reverse=int(str(num)[::-1])
if num==reverse:
    print("Number is palindrome")
else:
    print("Number is not palindrome")

