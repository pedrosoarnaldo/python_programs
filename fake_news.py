import criaDicionario
import eFake

lurl = ['http://g1.globo.com/politica/noticia/2010/12/lula-veta-projeto-que-incluia-cinco-vacinas-no-calendario-da-rede-publica.html']

for url in lurl:
    print('-'*255)
    print(f'{url}')
    print('-' *255)
    vRetornoDicionario = criaDicionario.criaDicionario(url)
    vRetornoClassifica = eFake.classificaUrl(url)

print(f'Cria Dicionario ---> {vRetornoDicionario}. Classifica URL {vRetornoClassifica}.')