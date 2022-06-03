import numpy as np
from math import abs

s = "Hello"
print(s)

def myfunc(x,y,z):
    return np.max(abs(x), abs(y), abs(z))

if "__name__"=="__main":
    x=0.
    y=1.
      z=-3.
    myfunc(x,y,z)
