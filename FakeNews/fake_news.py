import criaDicionario
import eFake
import mysql

mydb = mysql.connector.connect(user='root', password='Zse4nji9123!@#',
                               host='127.0.0.1',
                               database='fakenews')
mycursor = mydb.cursor()


lurl = ['https://economia.uol.com.br/noticias/redacao/2019/05/28/renegociacao-dividas-caixa.htm']


for url in lurl:
    sql = str(f"SELECT e_fake FROM documentos where url = '{url}'")
    mycursor.execute(sql)
    myresult = mycursor.fetchone()

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