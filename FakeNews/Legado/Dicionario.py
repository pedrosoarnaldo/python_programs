import requests
from DatabasePool import DatabasePool
import os, uuid, json
from pprint import pprint

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

        if str(request) == "<Response [200]>":
            return 1
        return 0

        return int(myresult[0])

    def checkwordatazure(word="Oi"):
        subscription_key = "507e05c58d0c49db8bab2becd59e9d54"
        text_analytics_base_url = "https://api-eur.cognitive.microsofttranslator.com/dictionary/lookup?api-version=3.0&from=pt&to=en"
        documents = [{"Text": word}]

        headers = {"Ocp-Apim-Subscription-Key": subscription_key}
        response = requests.post(text_analytics_base_url, headers=headers, json=documents)
        x = response.json()
        pprint(x)

        '''return response'''

        '''if str(request) == "<Response [200]>":
            return 1
        return 0'''


d = Dicionario
d.checkwordatazure()