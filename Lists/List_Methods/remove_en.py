#added by @Azharoo
#Python 3

"""
The remove() method searches for the given element in the list and removes the first matching element.
If the element(argument) passed to the remove() method doesn't exist, valueError exception is thrown.
"""

#Example 1: Remove Element From The List
# animal list
animal = ['cat', 'dog', 'rabbit', 'cow']

# 'rabbit' element is removed
animal.remove('rabbit')

#Updated Animal List
print('Updated animal list: ', animal)


#Example 2: remove() Method on a List having Duplicate Elements
# If a list contains duplicate elements, the remove() method removes only the first instance

# animal list
animal = ['cat', 'dog', 'dog', 'cow', 'dog']

# 'dog' element is removed
animal.remove('dog')

#Updated Animal List
print('Updated animal list: ', animal)


"""
Example 3: Trying to Delete Element That Doesn't Exist 
When you run the program, you will get the following error: 
ValueError: list.remove(x): x not in list
"""
# animal list
animal = ['cat', 'dog', 'rabbit', 'cow']

# Deleting 'fish' element
animal.remove('fish')

# Updated Animal List
print('Updated animal list: ', animal)