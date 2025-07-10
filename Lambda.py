# add_lambda=lambda x,y:x+y
# print(add_lambda(2,3))

# sub_lambda=lambda x,y:x-y
# print(sub_lambda(9,3))

# # lambda function for square
# square=lambda x:x**2
# print(square(5))

# Filter function
# numbers=[1,2,3,4,5]
# even_numbers=list(filter(lambda x:x%2==0,numbers))
# print(even_numbers)

# x=lambda x,y,z:x+y+z
# print(x(8,3,4))

# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))

# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)
# mytripler = myfunc(3)

# print(mydoubler(11))
# print(mytripler(11))

x=lambda a:a**3
print(x(3))