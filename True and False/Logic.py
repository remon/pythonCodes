from __future__ import print_function
#this is a logic table for (and, or)
#before run this example you must ****install library truths***
#in cmd run command pip install truths
from truths import Truths

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

print("-------------------------------------------------------")
print("""Example Prerequisite : please insatll truths library
          *Open CMD rum command pip install truths *""")
print("-------------------------------------------------------")

r = raw_input(" Are you install truths???? :) Y:Yes , N:NO :) ").strip().upper()

def emp(r):
    if r=="Y":
        print(Truths(['a', 'b', 'x']))
        print(Truths(['a', 'b', 'cat', 'has_address'], ['(a and b)', 'a and b or cat', 'a and (b or cat) or has_address']))
        print(Truths(['a', 'b', 'x', 'd'], ['(a and b)', 'a and b or x', 'a and (b or x) or d'], ints=False))
    else:
        print("------------------------")
        print("------------------------")
        print("Please to Install truths")
        print("------------------------")
        print("------------------------")
        print("------------------------")
    raw_input("")

        


print(emp(r)) 
