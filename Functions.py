# def myfun():
#     print("Hello")


# def addition():
#     print(2+3)


# def multiplication():
#     print(2*7)


# def car():
#     print("Glossy color")

# myfun()
# addition()
# multiplication()
# car()

# find the square of a given number
# def square():
#     n=int(input("Enter number"))
#     return print(n*n)
# square()

# find the qube of a given number
# def qube():
#     n=int(input("Enter number"))
#     return print(n**3)
# qube()

# string formatting
# Name="Alice"
# age=25
# message=f"My name is {Name} and I am {age} years old"
# print(message)


# print(Name.lower())
# print(Name.replace("Alice","Sharvi"))

# def my_function():
#   print("Hello from a function")

# my_function()

# Find the largest item from list
# Given:

# x = [4, 6, 8, 24, 12, 2]
# def large_item():
#     x = [4, 6, 28, 24, 12, 2]
#     print(max(x))

# large_item()

# Generate a Python list of all the even numbers between 4 to 30
def even_number():
    n=int(input("Enter number"))
    list=[]
    for i in range(1,n+1):
        if i%2==0:
            list.append(i)

    print("Even numbers",list)
even_number()
