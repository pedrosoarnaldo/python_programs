import htmlParser
from unicodedata import normalize
from Dicionario import Dicionario
from DatabasePool import DatabasePool

d = DatabasePool()

try:
    connector = d.open_connection()
    cursor = connector.cursor()
except:
    print("Unable to open database!")
    exit(0)

def criaDicionario(url):

    d = Dicionario()

    lAuthor = ['autor', 'autores', 'author', 'authors']
    lPublisher = ['publisher', 'copyright']

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

        if d.checkwordlocally(target) == 0:
            retornoDicionarioWeb = d.checkwordatweb(target)
            if retornoDicionarioWeb == 0:
                vInsere = input(str(f'A palavra {target} existe? '))
                if vInsere == 's' or vInsere == 'S':
                    sql = str(f"INSERT INTO words(name) VALUES ('{target}')")
                    cursor.execute(sql)
                    connector.commit()
                    vPalavrasInseridas = vPalavrasInseridas + 1
                else:
                    vIgnora = input(str('Ignora a palavra ou contabiliza como errada (I/C) ? '))
                    if vIgnora == 'C' or vIgnora == 'c':
                        vPalavrasErradas = vPalavrasErradas + 1
            else:
                f.write(f'Inserindo a palavra ----> {target}\n')
                sql = str(f"INSERT INTO words(name) VALUES ('{target}')")
                cursor.execute(sql)
                connector.commit()
                vPalavrasInseridas = vPalavrasInseridas + 1

    vHashDocumento = hash(target)
    vEfake = 2

    url = url[0:512]
    sql = str(f"INSERT INTO documentos(id_documento, url, num_palavras_erradas, num_palavras, tem_autor, tem_publicador, e_fake) VALUES "
              f"('{vHashDocumento}', '{url}', {vPalavrasErradas}, {vTotalWords}, {vAuthor}, {vPublisher}, {vEfake})")
    cursor.execute(sql)
    connector.commit()
    cursor.close()
    connector.close()
    return 1
