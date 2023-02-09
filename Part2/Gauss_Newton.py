import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df=pd.read_csv("Part1\Customers.csv")
df["Profession"]=df.Profession.astype("category").cat.codes
df["Gender"]=df.Gender.astype("category").cat.codes

# Define the X and y data
X = df.drop(["Income","CustomerID"], axis=1)
y = df['Income']


# Define the Gauss-Newton algorithm for Non-Linear Regressions
def gauss_newton(X, y, beta, max_iter=2000, tol=1e-8):
    for i in range(max_iter):
        y_hat=np.dot(X,beta)
        J=np.dot(-X.T,y-y_hat)
        H=np.dot(X.T,X)
        delta = np.dot(np.linalg.inv(H),J)
        beta -= delta
        if np.linalg.norm(delta) < tol:
            break
    return beta

# Initialize the beta parameters
beta = np.zeros(X.shape[1])

# Find the LSE estimates of the NLR parameters using the Gauss-Newton method
beta_hat = gauss_newton(X, y, beta)

# Make predictions using the estimated parameters
y_pred = np.dot(X,beta_hat)

# Plot the predictions against the actual values
plt.scatter(y, y_pred)
plt.xlabel('Actual Values')
plt.ylabel('Predictions')
plt.title('Income Predictions')
plt.show()
