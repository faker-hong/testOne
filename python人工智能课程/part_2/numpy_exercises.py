import numpy as np

# Create a 1000 x 20 ndarray with random integers in the half-open interval [0, 5001).
X = np.random.randint(0, 5001, (1000, 20))

# print the shape of X
print(X)


# Average of the values in each column of X
ave_cols = X.mean(axis=0)

# Standard Deviation of the values in each column of X
std_cols = X.std(axis=0)

# Print the shape of ave_cols
print(ave_cols.shape)

# Print the shape of std_cols
print(std_cols.shape)

# Mean normalize X
X_norm = (X - ave_cols) / std_cols


# Print the average of all the values of X_norm
print(X_norm.mean())

# Print the average of the minimum value in each column of X_norm
print(X_norm.min(axis=0))

# Print the average of the maximum value in each column of X_norm
print(X_norm.max(axis=0))


# Create a rank 1 ndarray that contains a random permutation of the row indices of `X_norm`
row_indices = np.random.permutation(X_norm.shape[0])


# Create a Training Set
X_train = X_norm[row_indices[:600], :]

# Create a Cross Validation Set
X_crossVal = X_norm[row_indices[600:800], :]

# Create a Test Set
X_test = X_norm[row_indices[800:], :]


# Print the shape of X_train
print(X_train.shape)

# Print the shape of X_crossVal
print(X_crossVal.shape)

# Print the shape of X_test
print(X_test.shape)