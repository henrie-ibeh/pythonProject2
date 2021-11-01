"""
Linear Regression
Polynomial Regression
Multiple Regression
"""
import numpy
from scipy import stats
from matplotlib import pyplot as plt
from sklearn.metrics import r2_score
from sklearn import linear_model
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

# Then make a list of the independent values and call this variable X.
# Put the dependent values in a variable called y.
X = df[['Weight', 'Volume']]
y = df['CO2']

'''
From the sklearn module we will use the LinearRegression() method to create a linear regression object.

This object has a method called fit() that takes the independent and dependent values as parameters 
and fills the regression object with data that describes the relationship:
'''
regr = linear_model.LinearRegression()
regr.fit(X, y)
# Now we have a regression object that are ready to predict CO2 values based on a car's weight and volume:
# predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)