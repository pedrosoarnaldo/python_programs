import criaDicionario
import eFake
from DatabasePool import DatabasePool

d = DatabasePool()

try:
    connector = d.open_connection()
    cursor = connector.cursor()
except:
    print("Unable to open database!")
    exit(0)

lurl = ['https://g1.globo.com/df/distrito-federal/noticia/2019/05/29/presos-envolvidos-em-massacre-de-manaus-sao-transferidos-para-penitenciaria-federal-de-brasilia.ghtml']

for url in lurl:
    sql = str(f"SELECT e_fake FROM documentos where url = '{url}'")
    cursor.execute(sql)
    myresult = cursor.fetchone()

    try:
        for x in myresult:
            if x >= 0:
                if x == 0:
                    print('Documento é fake!')
                else:
                    print('Documento não é fake!')
    except:
        print('-'*255)
        print(f'{url}')
        print('-' *255)
        vRetornoDicionario = criaDicionario.criaDicionario(url)
        vRetornoClassifica = eFake.classificaUrl(url)
        print(f'Cria Dicionario ---> {vRetornoDicionario}. Classifica URL {vRetornoClassifica}.')

    cursor.close()
    connector.close()
