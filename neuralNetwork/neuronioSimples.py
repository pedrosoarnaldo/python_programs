import numpy as np
from datetime import datetime

dtinicial = datetime.now()

# Define o número de épocas da simulação e o número de atributos
numEpocas = 65000
numAmostras = 6

# Atributos
peso = np.array([113, 122, 107, 98, 115, 120])
pH = np.array([6.8, 4.7, 5.2, 3.6, 2.9, 4.2])

# bias
bias = 1

# Entrada do Perceptron.
X = np.vstack((peso, pH))  # Ou X = np.asarray([peso, pH])
Y = np.array([[-1, 1], [1, 1], [-1, 1], [-1, 1], [1, -1], [1, 1]])

# Classes
# +1, +1 = C1
# -1, +1 = C2
# +1, -1 = C3

# Taxa de aprendizado.
eta = 0.1

# Array para amazernar os erros.
e = np.zeros(6)

# Define a matriz de pesos.
W = np.ones([2, 3])  # Duas entradas e o bias !

def funcaoAtivacao(valor):
    if valor < 0.0:
        return -1
    else:
        return 1


for j in range(numEpocas):
    for i in range(2):
        for k in range(numAmostras):
            # Insere o bias no vetor de entrada.
            Xb = np.hstack((bias, X[:, k]))

            # Calcula o vetor campo induzido.
            V = np.dot(W[0], Xb)

            # Degrau bipolar
            Yr = funcaoAtivacao(V)

            # Calcula o erro: e = (Y - Yr)
            e[k] = Y[k][0] - Yr

            # Treinando a rede.
            W[0] = W[0] + eta * e[k] * Xb
        #print("Peso ", W[i])

print("")
print("Peso ", W)

print("")
print("Vetor de errors (e) = " + str(e))
print("")

print("Minha entrada de dados tem que ser : 1")
ValidaEntrada = np.dot([-0.8, -19.6, -0.72], [1, 115, 2.9])
print("O valor estimado pela rede foi: ", funcaoAtivacao(ValidaEntrada))

print("")

print("Minha entrada de dados tem que ser : -1")
ValidaEntrada = np.dot([1,  2, 1.26], [1, 115, 2.9])
print("O valor estimado pela rede foi: ", funcaoAtivacao(ValidaEntrada))

print("")
print("Decorridos: ", datetime.now() - dtinicial)

print("")
acerto = 0
for i in range(numAmostras):
    if e[i] == 0:
        acerto = acerto + 1

tx_acerto = (acerto / numAmostras) * 100
print ("Taixa de acerto ", tx_acerto)