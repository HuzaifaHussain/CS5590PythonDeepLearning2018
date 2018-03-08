import csv
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
x = []
y = []
def pull_file(filename):
    with open(filename,'r') as csvdoc:
        csvInfile = csv.reader(csvdoc)
        next(csvInfile)
        for line in csvInfile:
            x.append(int(line[0]))
            y.append(int(line[1]))
    return
pull_file('pizzafranchise.csv')
select_model = linear_model.LinearRegression()
x = np.reshape(x,(len(x),1))
y = np.reshape(y,(len(y),1))
select_model.fit(x, y)
predicted_cost = select_model.predict(900)
coeff = select_model.coef_[0][0]
const = select_model.intercept_[0]
plt.scatter(x,y,color="blue",label="the values of data")
plt.scatter(900,select_model.predict(900),color="black",marker = "x",s=150,label="the output of forecast")
plt.plot(x,select_model.predict(x),color="red",label="Linear Regression")
plt.xlabel('Fees for Yearly Franchise')
plt.ylabel('Expense for starting up a Franchise')
plt.legend()
plt.show()