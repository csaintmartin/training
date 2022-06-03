import numpy as np 
from math import abs

s = "Hello"
print(s)

def myfunc(x,y,z):
    return np.max(abs(x), abs(y), abs(z))

