import json
import requests

def procuraPalavra(palavra):
    api_url = f'http://dicionario-aberto.net/search-json/{palavra}'
    resp = requests.get(api_url)
    if resp == '<Response [404]>':
        print('nao existe')
        return(0)
    else:
        '''response = resp.json()'''
        return(1)

''' x = procuraPalavra('ruas')
print(x)
'''
