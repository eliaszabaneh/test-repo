import numpy as np
import pandas as pd

# reading the dataset
dataset = pd.read_csv('../ML/50_Startups.csv')

# checking the top 5 rows
print(dataset.head())

# checking shape of the dataset
print(dataset.shape)

# defining input features (X) and output feature (y)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# checking the shape of input and output features
X_shape = X.shape
print('Shape of input features: ', X_shape)
y_shape = y.shape
print('Shape of output feature: ', y_shape)

# checking the input matrix
# print(X)

# One hot encoding ot the categorial column
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

# input feature matrix after categorial encoding
# print(X)

# Splitting the features into train and test sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# checking the shape of the training and test sets
print("Shape of training patterns: ", X_train.shape, y_train.shape)
print("Shape of test patterns: ", X_test.shape, y_test.shape)

# Defining a linear regression model
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

# Fitting the linear regression model
regressor.fit(X_train, y_train)

# Checking the regression coefficients od the fitted model
print("The regression coefficients are: ", regressor.coef_)

# Checking the intercept
print("The intercept is ", regressor.intercept_)

# Making predictions on the dataset
y_pred = regressor.predict(X_test)

# comparing the predicted profit with the actual profit
df = pd.DataFrame(data={'Predicted Profit': y_pred, 'Actual Profit': y_test})
print("**** Printing Data Frame ****")
print(df)
print("****                     ****")
# a_test = np.zeros((1,6))
# print("Testing with ", a_test , "The intercept is", regressor.predict(a_test))

# Mean Squared Error (MSE)
from sklearn.metrics import mean_squared_error

MSE = mean_squared_error(y_test, y_pred)

print("Mean Square Error is ", MSE)

# Root Mean Squared Error (RMSE)
import math

RMSE = math.sqrt(MSE)
print("Root Mean Squared Error is ", RMSE)

# R-Squared
from sklearn.metrics import r2_score

r2 = r2_score(y_test, y_pred)
print("R-Squared is ", r2)

# Adjusted R-Squared
adj = 1 - ((1 - r2) * (X_train.shape[0] - 1) / (X_train.shape[0] - X_train.shape[1] - 1))
print("Adjusted R-Squared is ", adj)

# Plotting the data
import matplotlib.pyplot as plt

plt.style.use('default')
plt.style.use('ggplot')

fig, ax = plt.subplots(figsize=(8, 4))

X_res = dataset['Marketing Spend'].values.reshape(-1, 1)
y_res = dataset['Profit'].values

X_dres = df['Predicted Profit'].values
y_dres = df['Actual Profit'].values
y_p = regressor.predict(X)
# ax.plot(dataset['Administration'].values, dataset['Profit'].values, color='k', label='Regression model')
print("X_test[:,4] is ", X_test[:, 4].shape, "-->", X_test[:, 4])
print("y_pred is ", y_pred.shape, "-->", y_pred)
ax.plot(X_test[:, 4], y_pred, color='b', label='Regression model')
ax.scatter(X_test[:, 4], y_pred, edgecolor='c', facecolor='y', alpha=0.7, label='Sample data')
ax.scatter(y_test, y_pred, edgecolor='r', facecolor='grey', alpha=0.7, label='Sample data')
ax.set_ylabel('Ys', fontsize=14)
ax.set_xlabel('Xs', fontsize=14)
ax.text(0.8, 0.1, 'test...', fontsize=13, ha='center', va='center', transform=ax.transAxes, color='grey', alpha=0.5)

ax.legend(facecolor='white', fontsize=11)
ax.set_title('$R^2 = %.2f$' % r2, fontsize=18)

fig.tight_layout()
fig.show()
