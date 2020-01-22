import numpy as np
import datetime as dt

def funcaoAtivacao(valor):
    if valor <= 0.0:
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

## Utilizado pelo programa neuronioJaTreinado.py

