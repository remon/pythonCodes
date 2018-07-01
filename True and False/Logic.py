#this is a logic table for (and, or)
#before run this example you must ****install library truths***
#in cmd run command pip install truths
import truths
from truths import Truths
print("-------------------------------------------------------")
print("""Example Prerequisite : please insatll truths library
          *Open CMD rum command pip install truths *""")
print("-------------------------------------------------------")

r = raw_input(" Are you install truths???? :) Y:Yes , N:NO :) ")

def emp(r):
    if r=="Y":
        print truths.Truths(['a', 'b', 'x'])
        print Truths(['a', 'b', 'cat', 'has_address'], ['(a and b)', 'a and b or cat', 'a and (b or cat) or has_address'])
        print Truths(['a', 'b', 'x', 'd'], ['(a and b)', 'a and b or x', 'a and (b or x) or d'], ints=False)
        input("")

    else:
        print("------------------------")
        print("------------------------")
        print("Please to Install truths")
        print("------------------------")
        print("------------------------")
        print("------------------------")
        input("")

        


print emp(r) 

