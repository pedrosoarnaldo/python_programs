from sklearn import tree
from DatabasePool import DatabasePool

def classificaUrl(url):

    d = DatabasePool()

    try:
        connector = d.open_connection()
        cursor = connector.cursor()
    except:
        print("Unable to open database!")
        exit(0)

    sql = str(f"SELECT id_documento, num_palavras_erradas, num_palavras, tem_autor, tem_publicador, e_fake FROM documentos where url <> '{url}' order by 1")
    cursor.execute(sql)
    myresult = cursor.fetchall()
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
    cursor.execute(sql)
    myresult = cursor.fetchone()

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
    cursor.execute(sql)
    connector.commit()
    cursor.close()
    connector.close()

    print('-'*30)
    return vResultado
