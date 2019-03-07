import criaDicionario

lurl = ['https://ultimosegundo.ig.com.br/brasil/2019-03-06/cameras-flagram-fugitivo-carnaval.html']

for url in lurl:
    print('---'*30)
    print(f'{url}')
    x = criaDicionario.criaDicionario(url)

if x == 1:
    print('Sucesso!')
