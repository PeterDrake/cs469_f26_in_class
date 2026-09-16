import numpy as np
from math import exp

def sigmoid(s):
    return 1 / (1 + exp(-s))

def neuron(inputs):
    # weights = np.array([-1.5, 1, 1])
    weights = (np.random.random(3) - 0.5) / 100
    return sigmoid(weights@inputs)

for inputs, teacher in zip((np.array([1, 0, 0]),
                            np.array([1, 0, 1]),
                            np.array([1, 1, 0]),
                            np.array([1, 1, 1])),
                           (0, 0, 0, 1)):  # Teachers
    print(f'{inputs} -> {neuron(inputs)}')
