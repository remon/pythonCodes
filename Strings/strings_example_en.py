#This file contains some examples for Python Strings 
#What is Strings in python ?
#Strings are amongst the most popular types in Python.
#We can create them simply by enclosing characters in quotes. 
#Python treats single quotes the same as double quotes. 
#Creating strings is as simple as assigning a value to a variable.
#source of Definition https://www.tutorialspoint.com/python/python_strings.htm

#example 1
#added by @remon
str1 ="Hello World"
print(str1)

#example 2
#added by @remon
str2 ='Hello World 2'
print(str2)

#example 3
#added by @remon
str3 ="2018"
print(str3)

#example 4
#added by @tony.dx.3379aems5
str4 = "Hello 2 My friends 3"
num1 = int(str4[str4.find("2")])
num2 = int(str4[-1])
result = num1 + num2 
print(result)