"""This is an example shows that every thing
in python is an object"""
# this is a python 3 code
mylist = ['a',  'b']
mybool = True
mynone = None

def myfunc():
    print('hello')

this = type(mylist)

print(type(mylist))
print(type(mybool))
print(type(mynone))
print(type(myfunc))
print(type(this))
