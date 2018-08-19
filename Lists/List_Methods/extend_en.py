#added by @Azharoo
#Python 3

"""
extend(): Iterates over its argument and adding each element to the list and extending the list. 
The length of the list increases by number of elements in it’s argument.

NOTE: A string is an iterable, so if you extend a list with a string, 
you’ll append each character as you iterate over the string.

This method does not return any value but add the content to existing list.
"""

#Example 1: Using extend() Method

aList = [123, 'xyz', 'abc', 78];
bList = [2018, 'Lolo'];
aList.extend(bList)
print ("Extended List : ", aList )  #Extended List :  [123, 'xyz', 'abc', 78, 2018, 'Lolo']


#Example 2:

my_list = ['python', 'codes', 1, 2, 3]
my_list.extend('Azharo')
print (my_list)  #['python', 'codes', 1, 2, 3, 'A', 'z', 'h', 'a', 'r', 'o']



#Example 3: Add Elements of Tuple and Set to List
#The native datatypes like tuple and set passed to extend() method is automatically converted to list. And, the elements of the list are appended to the end.

# language list
language = ['Arabic', 'English', 'French']

# language tuple
language_tuple = ('Spanish', 'German')

# language set
language_set = {'Chinese', 'Japanese'}

# appending elements of language tuple
language.extend(language_tuple)

print('New Language List: ', language) #New Language List:  ['Arabic', 'English', 'French', 'Spanish', 'German']

# appending elements of language set
language.extend(language_set)

print('Newest Language List: ', language) #Newest Language List:  ['Arabic', 'English', 'French', 'Spanish', 'German', 'Chinese', 'Japanese']



#Example 4: You can also add items of a list to another list using + or += operator.

a = [1, 2]
b = [3, 4]

a += b

print('a = ', a)  # Output: a = [1, 2, 3, 4]