import htmlParser
import mysql.connector
import testaPalavra
from unicodedata import normalize

mydb = mysql.connector.connect(user='root', password='Zse4nji9123!@#',
                              host='127.0.0.1',
                              database='fakenews')

mycursor = mydb.cursor()

url = "https://noticias.uol.com.br/politica/ultimas-noticias/2019/03/03/sigilo-e-escolta-os-preparativos-para-as-9-horas-de-lula-fora-da-prisao.htm"
freq = htmlParser.geraFrequencia(url)
vPalavrasErradas = 0
vPalavrasInseridas = 0

for key, val in freq.items(): 
    ''' print(key + ':' + str(val))
    freq.plot(10, cumulative=False)'''

    target = normalize('NFKD', key).encode('ASCII', 'ignore').decode('ASCII')

    sql = str(f"SELECT count(*) FROM words where name = '{target}'")
    ''' print(f'Palavra -> {target}') '''
    mycursor.execute(sql)

    myresult = mycursor.fetchone()

    for x in myresult:
        if x == 0:
            retornoDicionarioWeb = testaPalavra.palavraExiste(target)

            if retornoDicionarioWeb == 0:
                vInsere = input(str(f'A palavra {target} existe? '))
                if vInsere == 's' or vInsere == 'S':
                    sql = str(f"INSERT INTO words(name) VALUES ('{target}')")
                    mycursor.execute(sql)
                    mydb.commit()
                    vPalavrasInseridas = vPalavrasInseridas + 1
                else:
                    vPalavrasErradas = vPalavrasErradas + 1
            else:
                sql = str(f"INSERT INTO words(name) VALUES ('{target}')")
                mycursor.execute(sql)
                mydb.commit()
                vPalavrasInseridas = vPalavrasInseridas + 1

mydb.close()
print(f'Quantidade de palavras erradas: {vPalavrasErradas}')
print(f'Quantidade de palavras inseridas no dicionario: {vPalavrasInseridas}')
