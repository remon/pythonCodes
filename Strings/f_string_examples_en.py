# Here is an example for f-Strings in Python 3's.
# The name of the file is f_string_examples_en.py
# Added by @husseinhegazy in Github


# f-Strings:
# Is A New and Improved Way to Format Strings in Python 3's.

# The syntax is similar to the one you used with str.format() but less verbose.
# Look at how easily readable this Examples is:


name = "Hussein"
age = 32
print(f"Hello, {name}. You are {age}.")


# It would also be valid to use a capital letter F:
print(F"Hello, {name}. You are {age}.")


# You could do something pretty straightforward, like this:
print(f"{2 * 8 * 10}")


# You could also call functions. Here’s an example:
def to_lowercase(input):
    return input.lower()


name = "Hello World"
print(f"{to_lowercase(name)} is a simple program!!")


# You also have the option of calling a method directly:
name = "Hello World"
print(f"{name.lower()} is a simple program!!")
