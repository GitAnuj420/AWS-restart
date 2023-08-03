string = "This is my string"
print(string)
print(type(string))
print(string + " is of the data type "+str(type(string)))

firstString = "Yati pagal h"
secondString = "pr mera pyaar h"
thirdString = firstString + secondString
print(thirdString)
name = input("What is your name")
color = input("What is your fav color")
animal = input("What is your fav animal")
print("{}, you like a {} {} !" .format(name,color,animal))