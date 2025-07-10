# class Animal:
#     def speak(self):
#         print("Animal Speaks")

# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")

# dog=Dog()
# dog.speak()


class Vehicle:
    def sound(self):
        print("Bow")
class Car(Vehicle):
    def sound(self):
        print("Horn")
car=Car()
car.sound()


# class BankAccount:
#     def __init__(self,balance):
#         self._balance=balance

#     def deposit(self,amount):
#         if amount>0:
#             self._balance+=amount
#             print(f"Deposited:{amount}")

#     def get_balance(self):
#         return self._balance
# account=BankAccount(1000)

# account.deposit(500)
# print(account.get_balance())

# print(account._balance)

