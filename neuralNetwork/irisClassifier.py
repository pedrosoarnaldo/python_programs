import numpy as np
import csv

class irisClassifier:

    def __init__(self):
        # Parametros das petalas de rosa
        self.sepala_comprimento = []
        self.sepala_largura = []
        self.petala_comprimento = []
        self.petala_largura = []
        self.classe_da_flor = []
        self.file_name = 'iris.data'

    @staticmethod
    def iris_classifier(iris):
        if iris == [1, 1]:
            return "Iris-setosa"
        elif iris == [-1, -1]:
            return "Iris-versicolor"
        elif iris == [-1, 1]:
            return "Iris-verginica"
        else:
            return "unknown"

    def tree_loader(self, file_name):
        fo = open(file_name, 'r')
        lo = csv.reader(fo, delimiter=',')

        for c1, c2, c3, c4, c5 in lo:
            self.sepala_comprimento.append(float(c1))
            self.sepala_largura.append(float(c2))
            self.petala_comprimento.append(float(c3))
            self.petala_largura.append(float(c4))

            if c5 == "Iris-setosa":
                value = [1, 1]
            elif c5 == "Iris-versicolor":
                value = [-1, -1]
            else:
                # Iris-virginica
                value = [-1, 1]

            self.classe_da_flor.append(value)

