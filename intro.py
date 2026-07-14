import random
from array import *
# print("Hello, what is your name₹?")
# name = input()
# print("Your name is " + name)
# print(len(name))
# print("what is your age")
# age = input()
# print("you will be " + str(int(age) + 1) + " in a year")

# for i in name:
#    print (len(name)+1);


# num = random.randint(0,99) #generates a random integer between 0 and 99
# print (num)

# floatint = random.random() #generates a random floating point number between 0 and 1
# print (floatint)

# num2 = random.randrange(0,99,5)
# print(num2)

# car = random.choice(["BMW", "Ford", "Bentley"])
# print(car)

# num1 = random.randint(1,100)
# print(num1)

# fruits = random.choice(["apple","mango","pineapple","kiwi","lichi"])      
# print(fruits)                        

# #random dice
# selection = random.choice(["h","t"])
# print("enter your input")
# headortail = input().lower()

# if (selection == headortail):
#     print("you win")
# else:
#     print("you lose, the correct option was : " + selection)

#guessthenumber
# import random

# num1 = random.randint(1, 5)

# print("Enter a number between 1 and 5")
# your_guess = int(input())

# if num1 == your_guess:
#     print("Well done")
# else:
#     if num1 > your_guess:
#         print("Too low, guess again")
#     else:
#         print("Too high, guess again")

#     print("Enter the second guess. Careful! This is your final chance.")
#     second_guess = int(input())

#     if second_guess == num1:
#         print("You win")
#     else:
#         print(f"You lose. The number was {num1}")

# # tuples , lists and dictionaries 

# fruits_names = ("apple", "banana","avacado")  # this is a tuple() -> cannot be changed once declared 
# fruits_list = ["mango", "lichi", "kiwi"] # this is a list[]
# fruits_dictionary = {1:"guava", 2:"pomegranate", 3:"orange"} #this is a dictionary{}

# fruits_dictionary[1] = "pineapple" #this will change guava -> pineapple

#ch-1
# countries = ("india", "usa", "poland")
# print (countries)
# print("input any country out of the given ones")
# choice = input()
# print(countries.index(choice))

# #ch-2
# print("enter any index from 0 to 2")
# choice2 = int(input())
# print(countries[choice2])

# #ch-4
# subjects = ["eng", "hindi", "maths", "science", "sst"]
# print(subjects)
# dislikes = input("which subject out of the above you dont like?")
# removed_list = subjects.index(dislikes)
# del subjects[removed_list]
# print(subjects)

#Strings 

# fname = input("enter your first name ")
# print("your name has", len(fname), "characters in its name ")
# sname = input("Enter your second name ")
# print("your full name is ", fname,sname, " and length of your second name is ", len(sname))
# name = sname + fname
# print("length of fullname is ", len(name))

# nums = array ('i' ,[45, 245, 34,45])         

# print(nums.count(45))

#2d lists and arrays :
simple_array = [[2,1,4], [9,54,23], [947,23,4]]
print(simple_array)
simple_array[1].append(4)
print(simple_array) #this makes the new value as  : 9,54,23 -> 9,54,23,4

