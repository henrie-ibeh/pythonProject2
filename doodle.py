"""
def base(ops):
    sew = []
    new = [int(x) if x.lstrip('-').isnumeric() else x for x in ops]
    print(new)
    for f in new:
        if isinstance(f, int):
            sew.append(f)
        else:
            if f == "+":
                n = sew[-1] + sew[-2]
                sew.append(n)
            elif f == "D":
                sew.append(sew[-1] * 2)
            elif f == "C":
                sew.pop()
    print(sew)
    h = sum(sew)
    print(h)
    return h


g = ["5", "-2", "4", "C", "D", "9", "+", "+"]
base(g)
"""
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# Execute a method that returns some important key values of Linear Regression:
slope, intercept, r, p, std_err = stats.linregress(x, y)

'''
Create a function that uses the slope and intercept values to return a new value. 
This new value represents where on the y-axis the corresponding x value will be placed:
'''


def myfunc(g):
    return slope * g + intercept


myModel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, myModel)
plt.show()
