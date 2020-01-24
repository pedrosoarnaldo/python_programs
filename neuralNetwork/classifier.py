import numpy as np

class classifier():
    """"Class based on neural network to classify data"""

    def __init__(self):
        self.X = np.ones(1),
        self.eta = 0.1          # learning rate
        self.parameters = ([113, 122, 107, 98, 115, 120], [6.8, 4.7, 5.2, 3.6, 2.9, 4.2])
        self.results = [-1, 1, -1, -1, 1, 1]


    @staticmethod
    def activation_function(value):
        if value < 0.0:
            return -1
        else:
            return 1

    @staticmethod
    def error_rate(e):
        k = 0
        count = len([i for i in e if i > k])
        return int(count / e)


    @staticmethod
    def neuron(self, bias, parameters, results, eta):
        self.number_of_parameters = 0
        for i in parameters:
            self.X = np.dot(self.X, i)
            number_of_parameters = number_of_parameters + 1

        # neuron weight
        w = np.ones([1, self.number_of_parameters+1])

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

                # Insert bias
                xb = np.hstack((bias, self.X[:, k]))

                # Calcula o vetor campo induzido.
                v = np.dot(w, xb)

                # Degrau bipolar
                yr = self.activation_function(v)

                # Calcula o erro: e = (Y - Yr)
                e[k] = y[k] - yr

                # Treinando a rede.
                w = w + self.eta * e[k] * xb

                if epoch == 65000:
                #if self.error_rate(e) == 1:
                    condition = 0

        return [epoch, self.w]