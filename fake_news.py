import criaDicionario

lurl = ['http://terraeplana1.blogspot.com/2016/01/as-provas-da-terra-plana.html',
        'https://noticia-tv.com/entrevista-helen-sbt/?utm_source=taboola&utm_medium=PHYTO-2B-DESK-CP1&utm_campaign=ofuxico']

''' Testar essa url http://reverberarvida.blogspot.com/2016/05/padre-jesuita-critica-atitude-dos.html'''

for url in lurl:
    x = criaDicionario.criaDicionario(url)

if x == 0:
    print('Sucesso!')
