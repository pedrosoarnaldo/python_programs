import criaDicionario
import eFake

lurl = ['http://www.criacionismo.com.br/2019/05/genesis-ensina-que-o-sol-foi-criado-no.html',
        'http://www.revistacriacionista.org.br/scb/index.php/revista-criacionista-menu-st']

for url in lurl:
    print('-'*255)
    print(f'{url}')
    print('-' *255)
    vRetornoDicionario = criaDicionario.criaDicionario(url)
    vRetornoClassifica = eFake.classificaUrl(url)

print(f'Cria Dicionario ---> {vRetornoDicionario}. Classifica URL {vRetornoClassifica}.')