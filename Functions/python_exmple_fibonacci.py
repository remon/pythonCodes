import numpy as np
def fibonacci_cube(num):
    lis = [0,1]
    for i in range(2,num):
        lis.append(lis[i-2] + lis[i-1])
    return np.array(lis)**3
print fibonacci_cube(8)
