import urllib.request as urllib2
import nltk
import string
import lxml.html as lh
from lxml.html.clean import Cleaner as Limpador
from nltk.corpus import stopwords
import re

def limpaHTML(html):
    limp = Limpador()
    limp.javascript = True
    limp.style = True
    limp.html = True
    limp.page_structure = False
    limp.meta = False
    limp.safe_attrs_only = False
    limp.links = False
    doc = lh.fromstring(html)
    doc = limp.clean_html(doc)
    return doc.text_content()

def geraHtmlLimpo(u):
    html_page = urllib2.urlopen(u)
    raw = html_page.read()
    rr = limpaHTML(raw)
    return(rr)

def geraFrequencia(u):
    lAuthor = ['autor', 'autores', 'author', 'authors']
    lPublisher = ['publisher', 'copyright']
    lHtml = []

    vAuthor = 0
    vPublisher = 0

    ''' html_page = urllib2.urlopen(u) '''

    html_page = urllib2.urlopen(u)
    raw = html_page.read()
    rr = limpaHTML(raw)

    lHtml = str(raw).lower().split()[:]

    for author in lAuthor:
        for rawHtml in lHtml:
            if re.search(author, rawHtml.lower()):
                vAuthor = 1

    for publisher in lPublisher:
        for rawHtml in lHtml:
            if re.search(publisher, rawHtml.lower()):
                vPublisher = 1

    rr = str(rr).replace('.', '. ')
    rr = str(rr).replace('-', ' ')
    rr = str(rr).replace('/', ' ')

    ''' Tira a pontuação do texto'''

    translator = str.maketrans('', '', string.punctuation)

    tokens = [str(t).lower().translate(translator) for t in rr.split()]
    clean_tokens = tokens[:]

    for token in tokens:
        if token in stopwords.words('portuguese'):
            clean_tokens.remove(token)
        if token.isdigit():
            clean_tokens.remove(token)

    freq = nltk.FreqDist(clean_tokens)

    return (freq, vAuthor, vPublisher)

''' 
u = "https://noticias.uol.com.br/internacional/ultimas-noticias/2019/02/22/venezuela-acao-do-brasil-e-humanitaria-e-nao-visa-politica-diz-porta-voz.htm"
freq = geraFrequencia(u)

 for key, val in freq.items():
    print(key + ':' + str(val))

freq.plot(10, cumulative=False)'''




