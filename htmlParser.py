from html.parser import HTMLParser
import urllib.request as urllib2
# from urllib import urlopen

import lxml.html as lh
from lxml.html.clean import clean_html
from lxml.html.clean import Cleaner as Limpador


# https://www.programcreek.com/python/example/63565/lxml.html.clean.Cleaner
# https://rushter.com/blog/python-fast-html-parser/
# https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python

# funcao que limpa o html, este funcionou bem

def lxml_to_text(html):
    doc = lh.fromstring(html)
    doc = clean_html(doc)
    return doc.text_content()


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


# classe htmlparser, nao funciona muito bem pois deixa os CSS e JavaScript
class MyHTMLParser(HTMLParser):
    # Initializing lists
    lsStartTags = list()
    lsEndTags = list()
    lsStartEndTags = list()
    lsComments = list()
    lsData = list()

    # HTML Parser Methods
    def handle_starttag(self, startTag, attrs):
        self.lsStartTags.append(startTag)

    def handle_endtag(self, endTag):
        self.lsEndTags.append(endTag)

    def handle_startendtag(self, startendTag, attrs):
        self.lsStartEndTags.append(startendTag)

    def handle_comment(self, data):
        self.lsComments.append(data)

    def handle_data(self, data):
        # print("Encountered some data  :", data)
        self.lsData.append(data)


# cria o parser
# parser = MyHTMLParser()

u = "https://oglobo.globo.com/brasil/camara-derruba-decreto-sobre-sigilo-de-documentos-impoe-primeira-derrota-ao-governo-23464387"

html_page = urllib2.urlopen(u)

# Feeding the content
# parser.feed(str(html_page.read()))

raw = html_page.read()

# printing the extracted values
# print("Start tags", parser.lsStartTags)
# print(“End tags”, parser.lsEndTags)
# print(“Start End tags”, parser.lsStartEndTags)
# print(“Comments”, parser.lsComments)
# print("Data", parser.lsData)

# print(raw)
# rr = lxml_to_text(raw)
rr = limpaHTML(raw)
print(rr)

