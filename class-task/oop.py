# class Student:
#     college = "Webster University"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print("Student Created with Name:", self.name,"and Age:", self.age)
#     def has_graduated(self):
#         if self.age >= 22:
#             print(self.name, "has graduated")
#         else:
#             print(self.name, "has not graduated")
#
#
# student = Student("Himal Tamang", 25)
# student.has_graduated()
#
#
#

class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f"{self.name} is eating.")
    

    def sleep(self):
        print(f"{self.name} is sleeping.")



class Dog(Animal):
    def sleep(self):
        print(f"{self.name} also sleeps in a dog bed.")


animal = Animal("Generic Animal", "Unknown")
animal.eat()
animal.sleep()

dog = Dog("Buddy", "Dog")
dog.sleep()
