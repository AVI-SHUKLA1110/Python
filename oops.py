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
