import numpy as np

def funcaoAtivacao(valor):
    if valor < 0.0:
        return -1
    else:
        return 1

print("")
print("Maça")
print("Minha entrada de dados tem que ser : 1")
ValidaEntrada = np.dot([-2420.4,          116.6,        -2502.09999999], [1, 120, 4.3])
print("O valor estimado pela rede foi: ", funcaoAtivacao(ValidaEntrada))
print("Minha entrada de dados tem que ser : 1")
ValidaEntrada = np.dot([-6207.6,           79.8,         -448.26000001], [1, 120, 4.3])
print("O valor estimado pela rede foi: ", funcaoAtivacao(ValidaEntrada))

print("")
print("Minha entrada de dados tem que ser : -1")
ValidaEntrada = np.dot([-2420.4,          116.6,        -2502.09999999], [1, 113, 3.6])
print("O valor estimado pela rede foi: ", funcaoAtivacao(ValidaEntrada))
print("Minha entrada de dados tem que ser : -1")
ValidaEntrada = np.dot([-6207.6,           79.8,         -448.26000001], [1, 113, 3.6])
print("O valor estimado pela rede foi: ", funcaoAtivacao(ValidaEntrada))

print("")
print("laranja")
print("Minha entrada de dados tem que ser : 1")
ValidaEntrada = np.dot([-2420.4,         116.6,        -2502.09999999], [1, 120, 4.2])
print("O valor estimado pela rede foi: ", funcaoAtivacao(ValidaEntrada))
print("Minha entrada de dados tem que ser : 1")
ValidaEntrada = np.dot([-6207.6,           79.8,         -448.26000001], [1, 120, 4.2])
print("O valor estimado pela rede foi: ", funcaoAtivacao(ValidaEntrada))
