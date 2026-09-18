import numpy as np
from math import exp

inputs = (np.array([1, 0, 0]),
          np.array([1, 0, 1]),
          np.array([1, 1, 0]),
          np.array([1, 1, 1]))
teachers = (0, 1, 1, 1)
weights = (np.random.random(3) - 0.5) / 100
learning_rate = 0.1

def sigmoid(s):
    return 1 / (1 + exp(-s))

def neuron(input):
    return sigmoid(weights@input)

def train(input, teacher):
    # Run forward
    activation = neuron(input)
    # Calculate weight changes
    change = (-(teacher - activation) *
              activation *
              (1 - activation) *
              input
              )
    # Update weights
    global weights
    weights -= learning_rate * change

for input in inputs:
    print(f'{input} -> {neuron(input)}')
print('---')
for i in range(10000):
    for input, teacher in zip(inputs, teachers):
        train(input, teacher)
for input in inputs:
    print(f'{input} -> {neuron(input)}')
