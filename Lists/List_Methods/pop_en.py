#added by @Azharoo
#Python 3

"""
The pop() method removes and returns the element at the given index (passed as an argument) from the list.
If no parameter is passed, the default index -1 is passed as an argument which returns the last element.
"""

#Example 1: Print Element Present at the Given Index from the List

# programming language list
language = ['Python', 'Php', 'C++', 'Oracle', 'Ruby']

# Return value from pop() When 3 is passed
print('When 3 is passed:') 
return_value = language.pop(3)
print('Return Value: ', return_value)

# Updated List
print('Updated List: ', language)




#Example 2: pop() when index is not passed and for negative index

# programming language list
language = ['Python', 'Php', 'C++', 'Oracle', 'Ruby']


# When index is not passed
print('\nWhen index is not passed:') 
print('Return Value: ', language.pop())
print('Updated List: ', language)

# When -1 is passed Pops Last Element
print('\nWhen -1 is passed:') 
print('Return Value: ', language.pop(-1))
print('Updated List: ', language)

# When -3 is passed Pops Third Last Element
print('\nWhen -3 is passed:') 
print('Return Value: ', language.pop(-3))
print('Updated List: ', language)