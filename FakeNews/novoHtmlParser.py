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

    req = urllib2.Request(u, headers={'User-Agent': "Magic Browser"})
    html_page = urllib2.urlopen(req)
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
    rr = str(rr).replace('{', ' ')
    rr = str(rr).replace('}', ' ')

    ''' Tira a pontuação do texto'''

    translator = str.maketrans('', '', string.punctuation)

    tokens = [str(t).translate(translator) for t in rr.split()]
    clean_tokens_lower = []

    for token in tokens:
        if token not in stopwords.words('portuguese') or token.isdigit() != 'True':
            if (re.findall('^[A-Z]+', token) and re.findall('\w[a-z][A-Z]+', token)) or (re.findall('^[a-z]+', token) and re.findall('\w[a-z][A-Z]+', token)):
                print(f'Aqui ---> {token}')
                quebraPalavra = re.sub(r"([A-Z])", r" \1", token).split()
                for qp in quebraPalavra:
                    qp = str(qp).lower()
                    clean_tokens_lower.append(qp)
            else:
                clean_tokens_lower.append(token.lower())

    freq = nltk.FreqDist(clean_tokens_lower)

    return (freq, vAuthor, vPublisher)

u = 'https://noticias.uol.com.br/cotidiano/ultimas-noticias/2019/03/06/jovem-morto-em-tiroteio-entre-folioes-faria-teste-no-fla-e-ajudava-padrasto.htm'
(vFreq, vAuthor, vPublicher) = geraFrequencia(u)

for key, val in vFreq.items():
    print(key + ':' + str(val))

'''freq.plot(10, cumulative=False)'''




