#added by @Azharoo
#Python 3

"""
The append() method adds an item to the end of the list.
The item can be numbers, strings, another list, dictionary etc.

the append() method only modifies the original list. It doesn't return any value.
"""

#Example 1: Adding Element to a List

my_list = ['python', 'codes', 1, 2, 3]
my_list.append('Azharo')
print (my_list)  #['python', 'codes', 1, 2, 3, 'Azharo']


#Example 2: Adding List to a List

aList = [123, 'xyz', 'abc', 78];
bList = [2018, 'Lolo'];
aList.append(bList)
print ("Updated List : ", aList )  #Updated List :  [123, 'xyz', 'abc', 78, [2018, 'Lolo']]



""" Notes
1) The difference between append and extend

append:

Appends any Python object as-is to the end of the list (i.e. as a last element in the list).
The resulting list may be nested and contain heterogeneous elements (i.e. list, string, tuple, dictionary, set, etc.)

extend:

Accepts any iterable as its argument and makes the list larger.
The resulting list is always one dimensional list (i.e. no nesting) and it may contain heterogeneous elements in it (e.g. characters, integers, float) as a result of applying list(iterable).

2) Similarity between append and extend

Both takes exactly one argument.
Both modify the list in-place.
As a result, both returns None
"""