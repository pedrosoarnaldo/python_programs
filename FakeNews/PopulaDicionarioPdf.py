from typing import List, Any

import mysql.connector
import unidecode
from tika import parser

mydb = mysql.connector.connect(user='root', password='Zse4nji9123!@#',
                                host='127.0.0.1',
                                database='fakenews')

mycursor = mydb.cursor()

raw = parser.from_file('C:\\Users\\arnaldo.pedroso\\Downloads\\dict.pdf')
l = str([raw['content']])
i = 0

for word in l.split():
    if '\\' not in word:
        w = (str(word).lower().replace(',', '').replace('.', '').replace('?', '').replace('!', '').replace('-','').replace('(', '').replace(':', '').replace(';', '').replace(')', '').replace('`', ''))
        w = unidecode.unidecode(w)
        print('-> {}'.format(w))
        try:
            i += 1
            sql = str(f"INSERT INTO words(name) VALUES ('{w}')")
            mycursor.execute(sql)
            mydb.commit()
        except:
            i -= 1
            continue

print('Foram inseridas {} palavras no dicionario!'.format(i))
mydb.close()
