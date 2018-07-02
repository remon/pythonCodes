
# Added by @ammarasmro

# Comprehensions are very convenient one-liners that allow a user to from a
# whole list or a dictionary easily

# One of the biggest benefits for comprehensions is that they are faster than
# a for-loop. As they allocate the necessary memory instead of appending an
# element with each cycle and reallocate more resources in case it needs them

sample_list = [x for x in range(5)]
print(sample_list)
# >>> [0,1,2,3,4]

# Or to perform a task while iterating through items
original_list = ['1', '2', '3'] # string representations of numbers
new_integer_list = [int(x) for x in original_list]

# A similar concept can be applied to the dictionaries
sample_dictionary =  {x: str(x) + '!' for x in range(3) }
print(sample_dictionary)
# >>> {0: '0!', 1: '1!', 2: '2!'}

# Conditional statements can be used to preprocess data before including them
# in a list
list_of_even_numbers = [x for x in range(20) if x % 2 == 0 ]
print(list_of_even_numbers)
# >>> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
