from PoemClassifier import PoemClassifier
from sklearn import tree
import csv

lf = []
lc = []


def treeloader(filename):
    fo = open(filename, 'r')
    lo = csv.reader(fo, delimiter=';')

    for c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, \
        c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, \
        c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, \
        c31, c32, c33, c34, c35, c36, c37, c38, c39, c40, \
        c41, c42, c43, c44, c45, c46, c47, c48, c49, c50, \
        c51, c52, c53, c54, c55, c56, c57, c58, c59, c60, \
        c61, c62, c63, c64, c65, c66, c67, c68, c69, c70, \
        c71 in lo:
        lf.append([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20,
                   c21, c22, c23, c24, c25, c26, c27, c28, c29, c30,
                   c31, c32, c33, c34, c35, c36, c37, c38, c39, c40,
                   c41, c42, c43, c44, c45, c46, c47, c48, c49, c50,
                   c51, c52, c53, c54, c55, c56, c57, c58, c59, c60,
                   c61, c62, c63, c64, c65, c66, c67, c68, c69, c70])

        lc.append(c71)


treeloader('treeloader.csv')
clf = tree.DecisionTreeClassifier()
clf = clf.fit(lf, lc)

p = PoemClassifier

verso = [
"O Amor é fogo que arde sem se ver"
"É ferida que doí e não se sente",
"É um contentamento descontente,",
"É dor que desatina sem doer.",
"É um não querer mais que bem querer",
"É o solitário andar por entre a gente",
"Mas como causar pode o seu favor",
"nos corações humanos amizade,",
"Se tão contrário a si é o mesmo amor",
"Batatinha quando nasce espalha rama pelo chão",
"menininha quando dorme põe a mão no coração",
"Que conhece o que é verdade"
]

ld = []

for palavra in verso:
    a = p.linetoarray(palavra)
    li = a.split()
    for l in li:
        ld.append(l[:])
    while len(ld) <= 69:
        ld.append('0')
    print(ld)
    print(clf.predict([ld]))
    ld.clear()