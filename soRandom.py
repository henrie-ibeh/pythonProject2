import numpy
from scipy import stats
from matplotlib import pyplot as plt
from sklearn.metrics import r2_score
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
import pandas

df14 = pandas.read_csv(r"C:\Users\pc\Downloads\england-premier-league-2014-2015.csv")
df15 = pandas.read_csv(r"C:\Users\pc\Downloads\england-premier-league-2015-2016.csv")
df16 = pandas.read_csv(r"C:\Users\pc\Downloads\england-premier-league-2016-2017.csv")
df17 = pandas.read_csv(r"C:\Users\pc\Downloads\england-premier-league-2017-2018.csv")
df18 = pandas.read_csv(r"C:\Users\pc\Downloads\england-premier-league-2018-2019.csv")
df19 = pandas.read_csv(r"C:\Users\pc\Downloads\england-premier-league-2019-2020.csv")
df20 = pandas.read_csv(r"C:\Users\pc\Downloads\england-premier-league-2020-2021.csv")
df21 = pandas.read_csv(r"C:\Users\pc\Downloads\england-premier-league-2021-2022.csv")

# Then make a list of the independent values and call this variable X.
# Put the dependent values in a variable called y.

frames = [df14, df15, df16, df17, df18, df19, df20]
fullFrame = pandas.concat(frames)

shortFrame = fullFrame[['HOME_TEAM', 'AWAY_TEAM', 'FTR', 'FTHG', 'FTAG', 'HTR', 'H_ST', 'A_ST']]
X = shortFrame['H_ST']
y = shortFrame['FTHG']

mymodel = numpy.poly1d(numpy.polyfit(X, y, 3))

myline = numpy.linspace(1, 22, 100)

plt.scatter(X, y)
print(r2_score(y, mymodel(X)))
plt.plot(myline, mymodel(myline))
plt.show()




