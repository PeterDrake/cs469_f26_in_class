def neuron(x1, x2):
    return float(-0.5 * 1 + 1.0 * x1 + 1.0 * x2 >= 0)

for inputs in ((0, 0), (0, 1), (1, 0), (1, 1)):
    print(f'{inputs} -> {neuron(*inputs)}')
