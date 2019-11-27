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
"De tanto ver lavar a sobrinha"
"pequenininha em grande bacia,",
"quis imitar o banho da Mirinha,",
"que a mão batia n'água e sorria.",
"A Vovó Ana, então, na carinha,",
"passava a mão, sabão... sorria,",
"achava em tudo uma gracinha...",
"toalha, fralda e logo trazia",
"minha boneca para tomar",
"banho também, porém, no verão,",
"outro boneco, eu quis ganhar...",
"bem leve e grande... mas desmanchou",
"porque era feito com papelão",
"pus-me a chorar, meu sonho acabou!"
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