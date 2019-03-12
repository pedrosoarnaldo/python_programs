import criaDicionario
import eFake

lurl = ['https://www1.folha.uol.com.br/poder/2019/03/fala-de-bolsonaro-gera-critica-e-mourao-tenta-fazer-de-crise-assunto-interno.shtml']

for url in lurl:
    print('-'*255)
    print(f'{url}')
    print('-' *255)
    vRetornoDicionario = criaDicionario.criaDicionario(url)
    vRetornoClassifica = eFake.classificaUrl(url)

print(f'Cria Dicionario ---> {vRetornoDicionario}. Classifica URL {vRetornoClassifica}.')