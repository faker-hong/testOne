import numpy as np
from python人工智能课程.part4_Neural_Networks.Analyzing_Student_Data.StudentAdmissions import train_features, train_targets, test_targets, test_features


np.random.seed(42)


def sigmoid(x):
    return 1/(1+np.exp(-x))


n_records, n_features = train_features.shape
n_hidden = 2
epochs = 1000
learn_rate = 0.005
last_loss = None

weights_input_hidden = np.random.normal(scale=1/n_features**.5, size=(n_features, n_hidden))
weights_hidden_output = np.random.normal(scale=1/n_features**.5, size=n_hidden)


for e in range(epochs):
    del_w_i_h = np.zeros(weights_input_hidden.shape)
    del_w_h_o = np.zeros(weights_hidden_output.shape)
    for x, y in zip(train_features.values, train_targets):
        hidden_in = np.dot(x, weights_input_hidden)
        hidden_out = sigmoid(hidden_in)

        output_in = np.dot(hidden_out, weights_hidden_output)
        output_out = sigmoid(output_in)

        error = y - output_out

        error_term = error * output_out * (1 - output_out)

        hidden_error = np.dot(error_term, weights_hidden_output)

        hidden_error_term = hidden_error * (1-hidden_out) * hidden_out

        del_w_h_o += error_term * hidden_out
        del_w_i_h += hidden_error_term * x[:, None]
        print(hidden_error_term)
        print(x[:, None])
        break
    weights_hidden_output += learn_rate * del_w_h_o / n_records
    weights_input_hidden += learn_rate * del_w_i_h / n_records

    if (e % 100 == 0):
        hidden_out = sigmoid(np.dot(x, weights_input_hidden))
        out = sigmoid((np.dot(hidden_out, weights_hidden_output)))
        loss = np.mean((test_targets - out) ** 2)

        if last_loss and last_loss < loss:
            print("Train loss: ", loss, "  WARNING - Loss Increasing")
        else:
            print("Train loss: ", loss)
        last_loss = loss


hidden = sigmoid(np.dot(test_features, weights_input_hidden))
out = sigmoid((np.dot(hidden, weights_hidden_output)))
prediction = out > 0.5
accracy = np.mean(prediction == test_targets)
print("accracy:", accracy)