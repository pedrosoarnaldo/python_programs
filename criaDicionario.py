import htmlParser
import mysql.connector
import testaPalavra
from unicodedata import normalize


def criaDicionario(url):
    lAuthor = ['autor', 'autores', 'author', 'authors']
    lPublisher = ['publisher', 'copyright']

    mydb = mysql.connector.connect(user='root', password='Zse4nji9123!@#',
                                   host='127.0.0.1',
                                  database='fakenews')

    mycursor = mydb.cursor()

    f = open('dicionario_fake_news.log', 'a+')

    (freq, vAuthor, vPublisher) = htmlParser.geraFrequencia(url)

    vPalavrasErradas = 0
    vPalavrasInseridas = 0
    vTotalWords = 0

    for key, val in freq.items():
        '''print(key + ':' + str(val))
        freq.plot(10, cumulative=False)'''

        target = normalize('NFKD', key).encode('ASCII', 'ignore').decode('ASCII')
        vTotalWords = vTotalWords + 1

        sql = str(f"SELECT count(*) FROM words where name = '{target}'")
        '''print(f'Palavra -> {target}')'''

        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        retornoDicionarioWeb = 0

        for x in myresult:
            if x == 0:
                '''print(f'Erro ---> {target}')'''
                retornoDicionarioWeb = testaPalavra.palavraExiste(target)

                if retornoDicionarioWeb == 0:
                    vInsere = input(str(f'A palavra {target} existe? '))

                    if vInsere == 's' or vInsere == 'S':
                        sql = str(f"INSERT INTO words(name) VALUES ('{target}')")
                        mycursor.execute(sql)
                        mydb.commit()
                        vPalavrasInseridas = vPalavrasInseridas + 1
                    else:
                        vIgnora = input(str('Ignora a palavra ou contabiliza como errada (I/C) ? '))
                        if vIgnora == 'C' or vIgnora == 'c':
                            vPalavrasErradas = vPalavrasErradas + 1
                else:
                    f.write(f'Inserindo a palavra ----> {target}\n')
                    sql = str(f"INSERT INTO words(name) VALUES ('{target}')")
                    mycursor.execute(sql)
                    mydb.commit()
                    vPalavrasInseridas = vPalavrasInseridas + 1

    vHashDocumento = hash(target)
    vEfakeStr = input(str('Esse documento é fake (s/n/d)? '))

    if vEfakeStr == 'n' or vEfakeStr == 'N':
        vEfake = 0
    else:
        vEfake = 1

    url = url[0:512]
    sql = str(f"INSERT INTO documentos(id_documento, url, num_palavras_erradas, num_palavras, tem_autor, tem_publicador, e_fake) VALUES "
            f"('{vHashDocumento}', '{url}', {vPalavrasErradas}, {vTotalWords}, {vAuthor}, {vPublisher}, {vEfake})")
    mycursor.execute(sql)
    mydb.commit()
    mydb.close()

    print(f'Quantidade de palavras erradas: {vPalavrasErradas}')
    print(f'Quantidade de palavras inseridas no dicionario: {vPalavrasInseridas}')
    print(f'Author encontrado: {vAuthor}')
    print(f'Publisher encontrado: {vPublisher}')
    print(f'Quantidade de palavras: {vTotalWords}')
    return(1)
