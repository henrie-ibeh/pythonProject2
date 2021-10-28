"""
Linear Regression
Polynomial Regression
Multiple Regression
"""
import numpy
from scipy import stats
from matplotlib import pyplot as plt
from sklearn.metrics import r2_score
import pandas

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

'''
linear regression
'''
# creating a scatter plot with line of regression

slope, intercept, r, p, std_err = stats.linregress(x, y)


# The r value ranges from -1 to 1, where 0 means no relationship, and 1 (and -1)
# means 100% related
# if r is low then linear regression isn't usable for predictions

def myfunc(x):
    return slope * x + intercept


mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

# testing for future predictions:
print(myfunc(12))

'''
Polynomial Regression:
'''
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(1, 22, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

# R-Squared(r2_score); testing for how well data fits into polynomial regression:
print(r2_score(y, mymodel(x)))

# Predicting future values:
speed = mymodel(17)
print(speed)

'''
Multiple Regression
'''
# importing a file into pandas

df = pandas.read_csv(r"C:\Users\pc\Downloads\cars.csv")
print(df.head(10))
