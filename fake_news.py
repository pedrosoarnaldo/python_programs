import htmlParser

url = "https://noticias.uol.com.br/internacional/ultimas-noticias/2019/02/22/venezuela-acao-do-brasil-e-humanitaria-e-nao-visa-politica-diz-porta-voz.htm"
freq = htmlParser.geraFrequencia(url)

for key, val in freq.items():
    print(key + ':' + str(val))

freq.plot(10, cumulative=False)

