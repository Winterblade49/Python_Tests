import numpy as np

# Activation function: Sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of the sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)

# Simple Neural Network Class
class SimpleNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights
        self.weights_input_hidden = np.random.rand(input_size, hidden_size)
        self.weights_hidden_output = np.random.rand(hidden_size, output_size)

    def forward(self, X):
        # Forward propagation
        self.hidden_layer_activation = np.dot(X, self.weights_input_hidden)
        self.hidden_layer_output = sigmoid(self.hidden_layer_activation)

        self.output_layer_activation = np.dot(self.hidden_layer_output, self.weights_hidden_output)
        return sigmoid(self.output_layer_activation)

    def backward(self, X, y, output, learning_rate):
        # Backward propagation
        output_error = y - output
        output_delta = output_error * sigmoid_derivative(output)

        hidden_layer_error = output_delta.dot(self.weights_hidden_output.T)
        hidden_layer_delta = hidden_layer_error * sigmoid_derivative(self.hidden_layer_output)

        # Update weights
        self.weights_hidden_output += self.hidden_layer_output.T.dot(output_delta) * learning_rate
        self.weights_input_hidden += X.T.dot(hidden_layer_delta) * learning_rate

# Sample data for XOR problem
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Input
y = np.array([[0], [1], [1], [0]])  # Output

# Initialize the neural network
input_size = 2
hidden_size = 2
output_size = 1
learning_rate = 0.1

nn = SimpleNeuralNetwork(input_size, hidden_size, output_size)

# Training the neural network
for epoch in range(10000):
    output = nn.forward(X)
    nn.backward(X, y, output, learning_rate)

# Test the trained model
print("Output after training:")
print(nn.forward(X))
