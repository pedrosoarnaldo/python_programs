from sklearn import tree

lisa=1
irregular=0
maca=1
laranja=0

pomar=[[150, lisa], [130, lisa], [180, irregular], [160, irregular]]
resultado=[maca, maca, laranja, laranja]


clf = tree.DecisionTreeClassifier()
clf = clf.fit(pomar, resultado)

while True:
    peso = int(input('Peso: '))
    if peso == 999:
        break

    superficie = int(input('Superficie: 1->Lisa 0->Irregular :'))
    resultadoUsuario = clf.predict([[peso, superficie]])

    if resultadoUsuario == 1:
        vResultado = str(input('É uma maça certo? s/n: '))
    else:
        vResultado = str(input('É uma laranja certo? s/n: '))

    if vResultado == 'n':
        pomar = pomar + [[peso, superficie]]

print(pomar)