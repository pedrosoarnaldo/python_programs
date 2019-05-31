import requests
from DatabasePool import DatabasePool

class Dicionario:
    """Classe usada para criar um dicionário de palavras localmente"""

    def __init__(self, url="http://dicionario-aberto.net/search-json/"):
        self.url = url

    def checkwordatweb(self, word="oi"):
        request = requests.get(self.url+word)
        if str(request) == "<Response [200]>":
            return 1
        return 0

    def checkwordlocally(self, word="oi"):
        self.word = word

        d = DatabasePool()

        try:
            connector = d.open_connection()
            cursor = connector.cursor()
        except:
            print("Unable to open database!")
            exit(0)

        sql = (f"SELECT COUNT(*) FROM words WHERE name = '{word}'")
        cursor.execute(sql)
        myresult = cursor.fetchone()

        cursor.close()
        connector.close()

        return int(myresult[0])