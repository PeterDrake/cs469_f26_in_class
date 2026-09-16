import numpy as np

def neuron(inputs):
    weights = np.array([-0.5, 1, 1])
    return float(weights@inputs >= 0)

for inputs in (np.array([1, 0, 0]), np.array([1, 0, 1]), np.array([1, 1, 0]), np.array([1, 1, 1])):
    print(f'{inputs} -> {neuron(inputs)}')
