
import urllib.request as urllib2
import nltk
from nltk.corpus import stopwords
import string

import lxml.html as lh
from lxml.html.clean import Cleaner as Limpador

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


u = "https://noticias.uol.com.br/internacional/ultimas-noticias/2019/02/22/venezuela-acao-do-brasil-e-humanitaria-e-nao-visa-politica-diz-porta-voz.htm"

html_page = urllib2.urlopen(u)
raw = html_page.read()
rr = limpaHTML(raw)

rr = str(rr).replace('.', '. ')
rr = str(rr).replace('-', ' ')
rr = str(rr).replace('/', ' ')

''' precisa excluir 18h55atualizada 119h44:1    '''

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

for key, val in freq.items():
    print(key + ':' + str(val))

freq.plot(10, cumulative=False)

