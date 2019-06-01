from typing import List, Any

import mysql.connector
import unidecode


l = []
i = 0

'''Arquivo Texto que será usado para popular dicionario'''
f = open(r"C:\Users\arnaldo.pedroso\Downloads\Notas_Aula_01.txt", "r")


for word in f.read().split():
    w = (str(word).lower().replace(',', '').replace('.', '').replace('?', '').replace('!', '').replace('-', '').replace('(', '').replace(':', '').replace(';', '').replace(')', '').replace('`', ''))
    w = unidecode.unidecode(w)
    l.append(w)

f.close()

mydb = mysql.connector.connect(user='root', password='Zse4nji9123!@#',
                                host='127.0.0.1',
                                database='fakenews')
mycursor = mydb.cursor()

for word in l:
    try:
        i += 1
        sql = str(f"INSERT INTO words(name) VALUES ('{word}')")
        mycursor.execute(sql)
        mydb.commit()
    except:
        i -= 1
        continue

print('Foram inseridas {} palavras no dicionario!'.format(i))
mydb.close()