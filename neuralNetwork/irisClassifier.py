from datetime import datetime
import numpy as np
import csv
import neuralNetwork.neuronClassifier as nc

# Parametros das petalas de rosa
sepala_comprimento = []
sepala_largura = []
petala_comprimento = []
petala_largura = []
classe_da_flor = []

# Parametro de resultado da flor

def iris_classifier(iris):
    if iris == [1, 1]:
        return "Iris-setosa"
    elif iris == [-1, 1]:
        return "Iris-versicolor"
    elif iris == [-1, -1]:
        return "Iris-verginica"
    else:
        return "unknown"


def tree_loader(filename):
    fo = open(filename, 'r')
    lo = csv.reader(fo, delimiter=',')

    for c1, c2, c3, c4, c5 in lo:
        sepala_comprimento.append(float(c1))
        sepala_largura.append(float(c2))
        petala_comprimento.append(float(c3))
        petala_largura.append(float(c4))

        if c5 == "Iris-setosa":
            value = [1, 1]
        elif c5 == "Iris-versicolor":
            value = [-1, 1]
        else:
            # Iris-virginica
            value = [-1, -1]

        classe_da_flor.append(value)

### Inicio do programa

dtinicial = datetime.now()

tree_loader('iris.data')

# Atributos
scomprimento = np.array(sepala_comprimento)
slargura = np.array(sepala_largura)
pcomprimento = np.array(petala_comprimento)
plargura = np.array(petala_largura)

# Entrada do Perceptron
X = np.vstack((scomprimento, slargura, pcomprimento, plargura))


for i in range(2):
    result = []
    for k in classe_da_flor:
        result.append(k[i])

    [epoch, weight, error] = nc.neuronClassifier.neuron(1, X, result, 0.1, 0.99)
    print("")
    print(f"Neuronio {i}")
    print(f"Epocas: {epoch}")
    print(f"Peso: {weight}")
    print(f"Erro: {error}")

