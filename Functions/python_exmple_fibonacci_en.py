#this file print out the fibonacci of the function input

#importing numpy for execute math with lists
import numpy as np
#define the function that takes one input
def fibonacci_cube(num):
    #define a list that contains 0 and 1 , because the fibonacci always starts with 0 and 1
    lis = [0,1]
    #this for loop takes the range of the parameter and 2
    for i in range(2,num):
        #appending the sum of the previuos two numbers to the list
        lis.append(lis[i-2] + lis[i-1])
    #finally returning the cube of the fibonacci content
    return np.array(lis)**3
#calling the function with 8 as an example
fibonacci_cube(8)
