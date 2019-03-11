

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#Split intro training and testing data set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(ages, net_worths, test_size=0.1) #10% of dataset


reg = LinearRegression()
clf.fit(X_train,Y_train)

print("Predicted Y value if x=10:", reg.predict(10))
print("r-squared score:", reg.score(X_test,Y_test)) #r-squared explains Which percentage of the variance is explained by the model
print("slope", reg.coef_)
print("intercept:", reg.intercept_)

#Visualizing the LinearRegression

plt.scatter(X,Y)
plt.plot(X, reg.predict(X), color = 'blue', linewidth =3)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

#Split training data
