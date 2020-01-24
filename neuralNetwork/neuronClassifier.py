import numpy as np


class neuronClassifier:
    """"Class based on neural network to classify data"""

    def __init__(self) -> object:
        self.x = np.ones(1),
        self.eta = 0.1  # learning rate
        self.parameters = ([113, 122, 107, 98, 115, 120], [6.8, 4.7, 5.2, 3.6, 2.9, 4.2])
        self.results = [-1, 1, -1, -1, 1, 1]

    @staticmethod
    def activation_function(value):
        if value < 0.0:
            return -1
        else:
            return 1

    @staticmethod
    def hit_rate(e):
        k = 0.0
        count = len([i for i in e if i == k])
        return float(count / len(e))

    @staticmethod
    def neuron(bias, parameters, results, eta, hit):
        number_of_parameters = 0
        x = np.vstack([i for i in parameters])
        number_of_parameters = len(parameters)

        # neuron weight
        w = np.ones([1, number_of_parameters + 1])

        # number of samples
        number_of_samples = len(parameters[0])

        # classification of the samples
        y = results

        # error array
        e = np.ones(number_of_samples)

        # number of epochs
        epoch = 0

        condition = 1

        while condition == 1:
            epoch = epoch + 1
            for k in range(number_of_samples):

                # Insere o bias no vetor de entrada.
                xb = np.hstack((bias, x[:, k]))

                # Calcula o vetor campo induzido.
                v = np.dot(w, xb)

                # Degrau bipolar
                yr = neuronClassifier.activation_function(v)

                # Calcula o erro: e = (Y - Yr)
                e[k] = y[k] - yr

                # Treinando a rede.
                w = w + eta * e[k] * xb

                tx_hit = neuronClassifier.hit_rate(e)

            if tx_hit >= hit:
                condition = 0

        return [epoch, w, e]
