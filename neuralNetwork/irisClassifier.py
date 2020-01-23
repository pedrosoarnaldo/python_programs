from datetime import datetime
import numpy as np
import csv

# Parametros das petalas de rosa
sepala_comprimento = []
sepala_largura = []
petala_comprimento = []
petala_largura = []
classe_da_flor = []

def treeloader(filename):
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

treeloader('iris.data')


# Número de épocas
numEpocas = 65000

# Número de amostras
numAmostras = len(classe_da_flor)

# Atributos
scomprimento = np.array(sepala_comprimento)
slargura = np.array(sepala_largura)
pcomprimento = np.array(petala_comprimento)
plargura = np.array(petala_largura)

# bias
bias = 2

# Entrada do Perceptron
X = np.vstack((scomprimento, slargura, pcomprimento, plargura))

# Classificacao
Y = np.array(classe_da_flor)
# Taxa de aprendizado.
eta = 0.1

# Array para amazernar os erros.
e = np.ones([numAmostras, 2])

# Define a matriz de pesos.
W = np.ones([2, 5])         # Quatro entradas e o bias !


def funcaoativacao(valor):
    if valor < 0.0:
        return -1
    else:
        return 1


for i in range(2):
    for j in range(numEpocas):
        for k in range(numAmostras):
            # Insere o bias no vetor de entrada.
            Xb = np.hstack((bias, X[:, k]))

            # Calcula o vetor campo induzido.
            V = np.dot(W[i], Xb)

            # Degrau bipolar
            Yr = funcaoativacao(V)

            # Calcula o erro: e = (Y - Yr)
            e[k][i] = Y[k][i] - Yr

            # Treinando a rede.
            W[i] = W[i] + eta * e[k][i] * Xb


print("Vetor de errors (e) = " + str(e))
print("Pesos: ", W)
print("Decorridos: ", datetime.now() - dtinicial)

print("")
acerto = 0
for i in range(numAmostras):
    if e[i][0] == 0 and e[i][0] == e[i][1]:
        acerto = acerto + 1

tx_acerto = (acerto / numAmostras) * 100
print ("Taxa de acerto ", tx_acerto)