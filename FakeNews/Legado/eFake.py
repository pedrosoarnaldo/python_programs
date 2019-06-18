from sklearn import tree
import mysql.connector

def classificaUrl(url):
    mydb = mysql.connector.connect(user='root', password='Zse4nji9123!@#',
                                   host='127.0.0.1',
                                   database='fakenews')

    mycursor = mydb.cursor()

    sql = str(f"SELECT id_documento, num_palavras_erradas, num_palavras, tem_autor, tem_publicador, e_fake FROM documentos where url <> '{url}' order by 1")
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    arrayDimensaoWord = []
    arrayClassificacao = []

    for result in myresult:
        arrayDimensaoWord.append(list(result[1:5]))
        if result[5] == 0:
            arrayClassificacao.append(0)
        else:
            arrayClassificacao.append(1)

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(arrayDimensaoWord, arrayClassificacao)

    sql = str(f"SELECT num_palavras_erradas, num_palavras, tem_autor, tem_publicador FROM documentos "
              f"where url = '{url}'")
    mycursor.execute(sql)
    myresult = mycursor.fetchone()

    listaPredict = list(myresult)
    resultadoUsuario = clf.predict([[listaPredict[0], listaPredict[1], listaPredict[2], listaPredict[3]]])

    print('-'*30)
    if resultadoUsuario == 1:
        vResultado = str(input('É fake certo? s/n: '))
        if vResultado != 'S' or vResultado != 's':
            vResultado = 0
    else:
        vResultado = str(input('É real certo? s/n: '))
        if vResultado != 'S' or vResultado != 's':
            vResultado = 1

    sql = str(f"update documentos set e_fake = {vResultado} where url = '{url}'")
    mycursor.execute(sql)
    mydb.commit()
    mydb.close()

    print('-'*30)
    return vResultado
