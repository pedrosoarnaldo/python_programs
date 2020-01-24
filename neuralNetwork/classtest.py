import numpy as np
from datetime import datetime
from neuralNetwork.neuronClassifier import neuronClassifier as nc

peso = np.array([113, 122, 107, 98, 115, 120])
pH = np.array([6.8, 4.7, 5.2, 3.6, 2.9, 4.2])
y = np.array([-1, 1, -1, -1, 1, 1])

parameter = (peso, pH)

c = nc()

dtinicial = datetime.now()
r = c.neuron(1, parameter, y, 0.1)
print("Decorridos: ", datetime.now() - dtinicial)

epoch = r[0]
weight = r[1]
e = r[2]

print(f"Epochs: {epoch}")
print(f"Weight: {weight}")
print(f"Error: {e}")
