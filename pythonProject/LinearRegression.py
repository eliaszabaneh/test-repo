import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Reading the data
data = pd.read_csv('Data\\Experience_Salaries.csv')

print(data)

# Defining input and output features as X and y respectively
X = data.iloc[:, 1:-1].values
y = data.iloc[:, -1].values

# Checking the shape of input and output features
print('Shape of the input features:', X.shape)
print('Shape of the output features:', y.shape)

# #from sklearn.linear_model import LinearRegression
# Defining and fitting a linear regression model
lin_reg = LinearRegression()
lin_reg.fit(X, y)
# Visualizing the fitted linear regression model
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg.predict(X), color='blue')
plt.title('Experience Vs Salaries')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()

# #from sklearn.preprocessing import PolynomialFeatures
# Defining and fitting a polynomial regression model
poly_reg = PolynomialFeatures(degree=5)
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)
# Visualizing the fitted polynomial regression model
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color='blue')
plt.title('Experience Vs Salaries')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()
