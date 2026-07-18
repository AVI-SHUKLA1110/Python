#class - a blueprint for creating objects
#method - a function contained within a class 
class Dog:
    def __init__(self, name , breed , color):
     self.name = name
     self.breed = breed
     self.color = color

#objects for Dog class
dog1 = Dog("albert" , "Grey hound" , "Black")
dog2 = Dog("Rocky" , "German Shephard" , "Brown")

print(dog1.color, dog1.breed)
print(dog2.color, dog2.breed)


class Owner:
   def __init__(self, name , address , number):
      self.name = name
      self.address = address
      self.number = number

owner1 = Owner("aman" , "Gorakhpur" , "123")
owner2 = Owner("harsh" , "Ludhiana" , "456")


class Person:
   def __init__(self, name, age) : 
      self.name = name
      self.age = age
   def greet(self) :
      print(f"Hello, my name is {self.name} and my age is {self.age}")

person1 = Person("aman" , 26)
person2 = Person("hercueles" , 30)


