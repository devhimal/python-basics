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
#
# class Animal:
#
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#
#     def eat(self):
#         print(f"{self.name} is eating.")
#
#
#     def sleep(self):
#         print(f"{self.name} is sleeping.")
#
#
#
# class Dog(Animal):
#     def sleep(self):
#         print(f"{self.name} also sleeps in a dog bed.")
#
#
# animal = Animal("Generic Animal", "Unknown")
# animal.eat()
# animal.sleep()
#
# dog = Dog("Buddy", "Dog")
# dog.sleep()


# Aug 19, 2025 ( Tuesday )



class Grandparent:
    def grantparent(self):
        print("This is the grandparent class.")

class Parent(Grandparent):
    def parent(self):
        print("This is the parent class.")

class child(Parent):
    def child(self):
        print("This is the child class.")


c = child()
c.grantparent()
c.parent()
c.child()


# multiple inheritance

class fourwheeler:
    def four_wheeler(self):
        print("This is a four wheeler vehicle.")

class two_wheeler:
    def two_wheeler(self):
        print("This is a two wheeler vehicle.")

class car(fourwheeler, two_wheeler):
    def car(self):
        print("This is a car.")

m = car()
m.four_wheeler()
m.two_wheeler()

# polymorphism and function overloading

def add(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result

addition = add(1, 2, 3)
addition2 = add(1, 2, 3, 4, 5)
print("Addition of 1, 2, 3 is:", addition)
print("Addition of 1, 2, 3, 4, 5 is:", addition2)
