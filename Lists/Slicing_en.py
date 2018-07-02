#added by @Azharoo
#Python 3
# Python slicing is a computationally fast way to methodically access parts of your data.

#Create a list of science subjects and another list of integers from 1-10
subjects = ['IT-Science','physics','biology','mathematics']
x=list(range(1,11))


#slicing the entire list.
subjects[:]
['IT-Science', 'physics', 'biology', 'mathematics']
x[:]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Slicing from index 0 up to the last index with a step size of 2.
subjects[::2]
['IT-Science', 'biology']
x[::2]
[1, 3, 5, 7, 9]

#Slicing from index 9 down to the last index with a negative step size of 2.
x[9:0:-2]
[10, 8, 6, 4, 2]
"""Slicing from last index from the right of the list 
down to the last index of the left of the list with a
negative step size of 3."""
x[::-3]
[10, 7, 4, 1]
