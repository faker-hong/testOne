import numpy as np
from python人工智能课程.part4_Neural_Networks.Analyzing_Student_Data.StudentAdmissions import train_features, train_targets, test_targets, test_features


np.random.seed(42)


def sigmoid(x):
    return 1/(1 + np.exp(-x))



# Hyperparameters
n_hidden = 2  # number of hidden unit
epochs = 900
learnrate = 0.005

n_records, n_features = train_features.shape
last_loss = None

# Initialize weights
weights_input_to_hidden = np.random.normal(scale=1 / n_features ** .5, size=(n_features, n_hidden))
weights_hidden_to_output = np.random.normal(scale=1 / n_features ** .5, size=n_hidden)


for e in range(epochs):
    del_w_input_hidden = np.zeros(weights_input_to_hidden.shape)
    del_w_hidden_output = np.zeros(weights_hidden_to_output.shape)
    for x, y in zip(train_features.values, train_targets):
        # Forward pass
        # TODO: Calculate the output
        hidden_input = np.dot(x, weights_input_to_hidden)
        hidden_output = sigmoid(hidden_input)
        output = sigmoid(np.dot(hidden_output, weights_hidden_to_output))

        ## Backward pass ##
        # TODO: Calculate the network's prediction error
        error = y - output

        # TODO: Calculate error term for the output unit
        output_error_term = error * output * (1 - output)

        ## propagate errors to hidden layer

        # TODO: Calculate the hidden layer's contribution to the error
        hidden_error = np.dot(output_error_term, weights_hidden_to_output)

        # TODO: Calculate the error term for the hidden layer
        hidden_error_term = hidden_error * hidden_output * (1 - hidden_output)

        # TODO: Update the change in weights
        del_w_hidden_output += output_error_term * hidden_output
        del_w_input_hidden += hidden_error_term * x[:, None]

    # TODO: Update weights  (don't forget to division by n_records or number of samples)
    weights_input_to_hidden += learnrate * del_w_input_hidden / n_records
    weights_hidden_to_output += learnrate * del_w_hidden_output / n_records

    # Printing out the mean square error on the training set
    if e % (epochs / 10) == 0:
        hidden_output = sigmoid(np.dot(x, weights_input_to_hidden))
        out = sigmoid(np.dot(hidden_output,
                             weights_hidden_to_output))
        loss = np.mean((out - train_targets) ** 2)

        if last_loss and last_loss < loss:
            print("Train loss: ", loss, "  WARNING - Loss Increasing")
        else:
            print("Train loss: ", loss)
        last_loss = loss

# Calculate accuracy on test data
hidden = sigmoid(np.dot(test_features, weights_input_to_hidden))
out = sigmoid(np.dot(hidden, weights_hidden_to_output))
predictions = out > 0.5
accuracy = np.mean(predictions == test_targets)
print("Prediction accuracy: {:.3f}".format(accuracy))