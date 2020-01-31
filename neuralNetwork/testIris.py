from neuralNetwork.irisClassifier import irisClassifier as iC
import numpy as np
from neuralNetwork.neuronClassifier import neuronClassifier as nC

c = iC()

#bias
bias = 1
eta = 0.1
tx_hit = 0.975

def treina_modelo():
    c.tree_loader('iris.data')

    # Atributos
    scomprimento = np.array(c.sepala_comprimento)
    slargura = np.array(c.sepala_largura)
    pcomprimento = np.array(c.petala_comprimento)
    plargura = np.array(c.petala_largura)

    # Entrada do Perceptron
    X = np.vstack((scomprimento, slargura, pcomprimento, plargura))

    for i in range(2):
        result = []
        for k in c.classe_da_flor:
            result.append(k[i])

        [epoch, weight, error] = nC.neuron(bias, X, result, eta, tx_hit)
        print("")
        print(f"Neuronio {i}")
        print(f"Epocas: {epoch}")
        print(f"Peso: {weight}")
        print(f"Erro: {error}")


def valida_modelo(register_to_test, weight1, weight2):
    ### Adiciona o Bias
    register_to_test = np.hstack([bias, register_to_test])
    result_neuron_1 = np.dot(weight1, register_to_test)
    result_neuron_2 = np.dot(weight2, register_to_test)
    return [nC.activation_function(result_neuron_1), nC.activation_function(result_neuron_2)]


#treina_modelo()
# register to test
register = [5.1, 3.5, 1.4, 0.2] #Iris-setosa
weight1 = [0.7931,  -0.353784,  0.414752, -0.235118,  0.540142]
weight2 = [1., 0.3, 1.1, 2.3, 2.1]

register_tested = iC.iris_classifier(valida_modelo(register, weight1, weight2))
print(register_tested)


