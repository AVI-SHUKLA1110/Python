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

class user:
   def __init__(self,username, email , password):
    self.username = username
    self._email = email
    self.password = password

class accessmethods:
   def __init__(self, name):
     self.name = name
     self._name = name
     self.__name = name

   # def say_hi(self, user):
   #    print(f"Sending message to {user.username}: Hi {user.username}")
      
   # def clean_email(self):
   #     return self._email.lower().strip()
   
# user1 = user("dantheman", "dan@123", "use123")
# user2 = user("abhishek","ashikla693@gmail.com   ", "user1" )


#making data attributes protected - means not being able to read outside this class
#using getter and setter functions 
method1 = accessmethods("thetechnofeak")
print(method1.name)
print(method1._name)
print(method1.__name)