#added by @Azharo
#Python 3

# How to find the most frequent element in a list

from collections import Counter

#Example 1:

my_groceries = ['apple', 'banana', 'banana', 'orage', 'banana', 'apple', 'beet', 'carrot', 'ginger', 'kale', 'ginger', 'ginger', 'kale', 'ginger']

print('Here are my groceries...\n')
print(my_groceries)

counter_thingy = Counter(my_groceries)


# list of all tuples/pairs in descending order of how commonly they showed up
print('\nHere is a list of all the tuples/pairs in descending order of how commonly each fruit showed up...\n')

print(counter_thingy.most_common())


# find the most common element
print('\nFind the most common element. If there is a tie, it will pick randomly...\n')
print(counter_thingy.most_common(1))


#Example 2:


# Real world use case.
# Let's say you are trying to create a word counter.
# This counter should show how frequently each word was used with.

sentence = '''Python is an interpreted high-level programming language for general-purpose 
programming . It provides constructs that enable clear programming on both small and large scales . 
Python features a dynamic type system and automatic memory management . 
It supports multiple programming paradigms, including object-oriented, imperative, 
functional and procedural, and has a large and comprehensive standard library .'''

# Here's how to solve this

# 1 - Turn it into a list of words
# 2 - Turn it into a counter object
# 3 - Print out how frequently each word is used

list_of_words = sentence.split()

counter_thingy = Counter(list_of_words)


#Print out how frequently each word is used as list of tuples

print('\nPrint out how frequently each word is used as list of tuples...\n')
print(counter_thingy.most_common())


# turn it into a dictionary instead of a list of tuples...

print('\n turn it into a dictionary instead...\n')
print(dict(counter_thingy.most_common()))

# find the most common element
print(counter_thingy.most_common(1))

