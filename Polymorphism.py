# class Cat:
#     def speak(self):
#         print("Meaw")

# class Dog:
#     def speak(self):
#         print("Woof")

# animals=[Cat(),Dog()]
# for animal in animals:
#     animal.speak()

class Train:
    def sound(self):
        print("Awaoooo")
class Airoplane(Train):
    def sound(self):
        print("Hawoooo")
class Car(Train):
    def sound(self):
        print("Bee Bee")
Vehicles=[Train(),Airoplane(),Car()]
for vehicle in Vehicles:
    vehicle.sound()
