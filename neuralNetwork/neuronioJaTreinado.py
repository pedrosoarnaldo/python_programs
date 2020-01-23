import numpy as np
import datetime as dt


def validaflor(valor):
    print("Valor --->", valor)
    if valor == [1, 1]:
        print("Iris-setosa")
    elif valor == [-1, 1]:
        print("Iris-versicolor")
    elif valor == [1, -1]:
        print("Iris-virginica")
    else:
        print("Erro")


def funcaoAtivacao(valor):
    if valor < 0.0:
        return -1
    else:
        return 1

dtinicio = dt.datetime.now()

## Utilizado pelo programa example01_simplePerceptron.py

ValidaEntrada = np.dot([-2420.4, 116.6, -2502.09999999], [1, 122, 6.8])
print("Valor esperado da minha entrada é -1. Valor encontrado ", funcaoAtivacao(ValidaEntrada))

ValidaEntrada = np.dot([-2420.4, 116.6, -2502.09999999], [1, 122, 4.7])
print(f"Valor esperado da minha entrada é 1. Valor encontrado ", funcaoAtivacao(ValidaEntrada))


dtfim = dt.datetime.now()

print("Decorridos: ", dtfim-dtinicio)

print("")
print("Valor esperado da minha entrada é Iris-Setosa")

## Utilizado pelo programa irisClassifier.py
ValidaEntrada1 = funcaoAtivacao(np.dot([100.,   -70.8,   60.4,    3.4,  141.8], [1,4.6,3.1,1.5,0.2]))
ValidaEntrada2 = funcaoAtivacao(np.dot([1228.,   97.9,  245.4, -341.3, -569.7], [1,4.6,3.1,1.5,0.2]))
print("Encontrado: ")
validaflor([ValidaEntrada1, ValidaEntrada2])







