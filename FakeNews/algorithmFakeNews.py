from fakenews import fakenews
from myHmlClass import myHtmlClass

url = "https://www1.folha.uol.com.br/mercado/2019/06/relator-admite-excluir-estados-e-municipios-de-reforma-da-previdencia.shtml"

t = myHtmlClass()
text = t.hml_cleaner(url)

try:
    f = fakenews()
except:
    print(f'Error trying to open url: {url}!')
    exit(0)

dimension_language = f.check_language(url, text)
dimension_sentiment = f.check_sentiment(url, text)
dimension_key_words = f.check_key_words(url, text)

print(dimension_language)
print(dimension_sentiment)
print(dimension_key_words)
