import htmlParser

def procuraPalavra(palavra):
    api_url = f'https://dicionario.priberam.org/{palavra}'
    rr = htmlParser.geraHtmlLimpo(api_url)
    return(rr)

def palavraExiste(palavra):
    r = procuraPalavra(palavra)
    lista = str(r).split('    ')

    stringRetorno = lista[896].split('.')

    if stringRetorno[0] == 'Palavra não encontrada':
        return(0)
    else:
        return(1)

