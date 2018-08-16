# this class has variable attributes like name and age you can define them with your input
# also has a default attributes like balance and credit but you can change them in a specific 
# object
# creat a new file for the class, then run my object in python's default idle
class student:
    #__init__ is a constructor that works by itself means initialze the class in the memory
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.balance = 0
        self.credit = 50

# here is my object
# try it python's default idle
s = student('ahmed', 25)
s.balance
s.credit
# you can change default values for ahmed, remove hashtag to try
# s.balance = 5