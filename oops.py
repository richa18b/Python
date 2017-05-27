import random
import sys
import os

class Animal :
    _name = None #this is equivalent to __name = ""
    _height = 0 #_ means that it is a private variable
    _weight = 0
    _sound = ""

    #constructor
    def __init__(self,name,height,weight,sound):
        self._name = name
        self._height = height
        self._weight = weight
        self._sound = sound

    #Getters and Setters for all attributes
    def get_name(self):
        print(self._name)

    def set_name(self, name):
        self._name = name

    def get_height(self):
        print(self._height)

    def set_height(self, height):
        self._height = height

    def get_weight(self):
        print(self._weight)

    def set_weight(self, weight):
        self._weight = weight

    def get_sound(self):
        print(self._sound)

    def set_sound(self, sound):
        self._sound = sound

    def get_type(self):
        print('Animal')

    def toString(self):
        return "{} is {} cms tall, {} kgs in weight and says {}".format(self._name,
                                                                        self._height,
                                                                        self._weight,
                                                                        self._sound)

cat = Animal('Cat',33,10,'Meoww')

print(cat.toString())

#Inheritance
class Dog(Animal):
    _owner = ""

    def __init__(self,name,height,weight,sound,owner):
        self._owner = owner
        super(Dog,self).__init__(name,height,weight,sound)

    def set_owner(self,owner):
        self._owner = owner

    def get_owner(self):
        return self._owner

    def get_type(self):
        print('Dog')

    #Overriding the function that's in the super class
    def toString(self):
        return "{} is {} cms tall, {} kgs in weight and says {}. His owner is {}".format(self._name,
                                                                                         self._height,
                                                                                         self._weight,
                                                                                         self._sound,
                                                                                         self._owner)

    #Performing method overloading
    def multiple_sounds(self,how_many = None): #A way of saying that we do not require attributes to be passed in our function
        if how_many is None :
            print(self.get_sound())
        else :
            print(self.get_sound() * how_many)

spot = Dog("Spot",53,27,"Ruff","Ash")

print(spot.toString())

#Polymorphism
class AnimalTesting :
    def get_type(self,animal) :
        animal.get_type()

test_animals = AnimalTesting()

test_animals.get_type(cat)
test_animals.get_type(spot)
