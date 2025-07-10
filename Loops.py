# for i in range(5):
#     print(i)

#     fruits = ["apple", "banana", "cherry"]
# for char in "banana":
#     print(char)

# for i in range(2):
#     for j in range(2):
#         print(i,j)

# print 1 to 25 numbers in reverse order.
# count=25
# while count>=1:
#     print(count)
#     count-=1

# Print first 10 natural numbers using while loop
# count=1
# while count<=10:
#     print(count)
#     count+=1

# Print the following pattern
# row=5
# for i in range(1,row+1,1):
#     for j in range(1,i+1):
#         print(j, end='')
#     print("")

# Calculate sum of all numbers from 1 to a given number
# number=int(input("Enter the numbers"))
# var=sum(range(1,number+1))
# print(var)

# Print multiplication table of a given number
# n=int(input("Enter the number"))
# for i in range(1,11,1):
#     table=n*i
#     print(table)

# Display numbers from a list using a loop
# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     print(i)

# Count the total number of digits in a number
# n=int(input("Enter number"))
# c=0
# while n!=0:
#     n=n//10
#     c=c+1
# print("Total number of digit=",c)

# Print Full Multiplication Table
# n=int(input("Enter number"))
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end="")
#     print()

# Find the sum of a series of a number up to n terms
# n=int(input("Enter number"))
# sum=0
# i=1
# while i<=n:
#     sum+=i
#     i=i+1
# print("Sum of the series",sum)

# for i in range(5):
#         for j in range(i+1):
#             print("*", end=" ")
#         print()

for i in range(5, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

for i in range(5):
        for j in range(5 - i - 1):
            print(" ", end=" ")
        for k in range(2 * i + 1):
            print("*", end=" ")
        print()

print("Welcome to", end = ' ')
print("GeeksforGeeks", end= ' ')

