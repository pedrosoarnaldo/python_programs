from sklearn import tree
import mysql.connector

def classificaUrl(url):
    mydb = mysql.connector.connect(user='root', password='Zse4nji9123!@#',
                                   host='127.0.0.1',
                                   database='fakenews')
    mycursor = mydb.cursor()


    sql = str(f"SELECT id_documento, num_palavras_erradas, num_palavras, tem_autor, tem_publicador, e_fake FROM documentos order by 1")
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    print(myresult)

    return(1)

'''
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
'''