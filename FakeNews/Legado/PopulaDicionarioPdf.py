import unidecode
from tika import parser
from DatabasePool import DatabasePool

d = DatabasePool()
connector = d.open_connection()
cursor = connector.cursor()

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
            cursor.execute(sql)
            connector.commit()
        except:
            i -= 1
            continue

print('Foram inseridas {} palavras no dicionario!'.format(i))
connector.commit()
cursor.close()
