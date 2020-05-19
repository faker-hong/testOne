import numpy as np


# Activation (sigmoid) function
def sigmoid(x):
    return 1/(1 + np.exp(-x))


# Output (prediction) formula
def output_formula(features, weights, bias):
    return sigmoid(np.dot(features, weights) + bias)


# Error (log-loss) formula
def error_formula(y, output):
    return -y*np.log(output)-(1-y)*np.log(1-output)


# Gradient descent step
def update_weights(x, y, weights, bias, learnrate):
    output = output_formula(x, weights, bias)
    d_error = -(y-output)
    weights -= learnrate * d_error * x
    bias -= learnrate*d_error
    return weights, bias