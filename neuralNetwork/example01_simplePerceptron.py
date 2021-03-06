# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 18:24:00 2018

@author: jmarcos
"""
import numpy as np
from datetime import datetime

dtinicial = datetime.now()

# Define o número de épocas da simulação e o número de atributos
numEpocas = 65000  # 70000
numAmostras = 6

# Atributos
peso = np.array([113, 122, 107, 98, 115, 120])
pH = np.array([6.8, 4.7, 5.2, 3.6, 2.9, 4.2])

# For debugging purposes.
normaliza = False
if normaliza:
    peso = peso / np.linalg.norm(peso)
    pH = pH / np.linalg.norm(peso)

# bias
bias = 1

# Entrada do Perceptron.
X = np.vstack((peso, pH))  # Ou X = np.asarray([peso, pH])
Y = np.array([-1, 1, -1, -1, 1, 1])

# Taxa de aprendizado.
eta = 0.1

# Array para amazernar os erros.
e = np.zeros(6)

# Define a matriz de pesos.
W = np.ones([1, 3])  # Duas entradas e o bias !


def funcaoAtivacao(valor):
    if valor < 0.0:
        return -1
    else:
        return 1


for j in range(numEpocas):
    for k in range(numAmostras):
        # Insere o bias no vetor de entrada.
        Xb = np.hstack((bias, X[:, k]))

        # Calcula o vetor campo induzido.
        V = np.dot(W, Xb)

        # Calcula a saída do perceptron.
        # Sigmoide
        #Yr = np.sign(V)

        # Degrau bipolar
        Yr = funcaoAtivacao(V)

        # Degrau bipolar ----- NÃO ENTENDI COMO USAR
        # Yr = np.heaviside(V, 1)

        # Tangenge hiberbolica
        #Yr = np.tanh(V)

        # Calcula o erro: e = (Y - Yr)
        e[k] = Y[k] - Yr

        # Treinando a rede.
        W = W + eta * e[k] * Xb

print(f"Peso {W}")
print("Vetor de errors (e) = " + str(e))

print("Minha entrada de dados tem que ser : -1")
ValidaEntrada = np.dot([-2420.4, 116.6, -2502.09999999], [1, 113, 6.8])

print("O valor estimado pela rede foi: ", funcaoAtivacao(ValidaEntrada))
print("Decorridos: ", datetime.now() - dtinicial)