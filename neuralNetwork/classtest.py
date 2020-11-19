import numpy as np
from datetime import datetime
import neuralNetwork.neuronClassifier as nc

hit = 0.9

peso = np.array([113, 122, 107, 98, 115, 120])
pH = np.array([6.8, 4.7, 5.2, 3.6, 2.9, 4.2])
y = np.array([-1, 1, -1, -1, 1, 1])
y1 = np.array([-1, 1, 1, -1, 1, 1])

### maca = [-1, -1]
### laranja = [ 1, 1 ]
### pera = [ -1, 1 ]

# 113 - 6.8 Maca
# 122 - 4.7 Laranja
# 107 - 5.2 pera
# 98 - 3.6  maca
# 115 - 2.9 laranja
# 120 - 4.2 laranja

parameter = (peso, pH)

c = nc.neuronClassifier()

dtinicial = datetime.now()

n = c.neuron(1, parameter, y, 0.1, hit)
epoch = n[0]
weight = n[1]
e = n[2]

n1 = c.neuron(1, parameter, y1, 0.1, hit)
epoch1 = n1[0]
weight1 = n1[1]
e1 = n1[2]

print("Decorridos: ", datetime.now() - dtinicial)

print(f"Epochs: {epoch}")
print(f"Weight: {weight}")
print(f"Error: {e}")

print(f"Epochs: {epoch1}")
print(f"Weight: {weight1}")
print(f"Error: {e1}")
