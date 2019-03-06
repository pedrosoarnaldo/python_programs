import criaDicionario

lurl = ['http://noticia-agora.com/kifina/blog/fibras-naturais-ml/?s1=548349647002106250&img=fibra-1&h=12&utm_source=Outbrain&utm_medium=BR_Portal%20IG_iG&utm_campaign=Cp5-Desk-Ren31&utm_content=Fibra%20natural%20rara%20obriga%20o%20corpo%20a%20eliminar%20gordura']


for url in lurl:
    x = criaDicionario.criaDicionario(url)

if x == 1:
    print('Sucesso!')
