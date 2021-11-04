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
from sklearn.preprocessing import StandardScaler
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

'''
Coefficient
The coefficient is a factor that describes the relationship with an unknown variable.

Example: if x is a variable, then 2x is x two times. x is the unknown variable, and the number 2 is the coefficient.

In this case, we can ask for the coefficient value of weight against CO2, and for volume against CO2.
The answer(s) we get tells us what would happen if we increase, or decrease, one of the independent values.
'''
# Print the coefficient values of the regression object:
print(regr.coef_)

'''
The result array represents the coefficient values of weight and volume.

Weight: 0.00755095
Volume: 0.00780526

These values tell us that if the weight increase by 1kg, the CO2 emission increases by 0.00755095g.

And if the engine size (Volume) increases by 1 cm3, the CO2 emission increases by 0.00780526 g.
'''

'''
Scale Features
When your data has different values, and even different measurement units, 
it can be difficult to compare them. What is kilograms compared to meters? Or altitude compared to time?
the same data set that we used in the multiple regression chapter,
but this time the volume column contains values in liters instead of cm3 (1.0 instead of 1000).
'''
# z = (x - u) / s
#
# Where z is the new value, x is the original value, u is the mean and s is the standard deviation.
#


# Scale all values in the Weight and Volume columns:
scale = StandardScaler()
scaledX = scale.fit_transform(X)

# When the data set is scaled, you will have to use the scale when you predict values:
regr.fit(scaledX, y)

# Predict the CO2 emission from a 1.3 liter car that weighs 2300 kilograms:
scaled = scale.transform([[2300, 1.3], [3300, 2.3]])
print("\n", scaled, "\n")
predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)

"""
Evaluate Your Model
In Machine Learning we create models to predict the outcome of certain events, 
like in the previous chapter where we predicted the CO2 emission of a car when we knew the weight and engine size.

To measure if the model is good enough, we can use a method called Train/Test.
Train/Test is a method to measure the accuracy of your model.

It is called Train/Test because you split the the data set into two sets: a training set and a testing set.

80% for training, and 20% for testing.

You train the model using the training set.

You test the model using the testing set.

Train the model means create the model.

Test the model means test the accuracy of the model.
"""


