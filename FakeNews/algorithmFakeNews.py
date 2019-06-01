from fakenews import fakenews
from myHmlClass import myHtmlClass

url = "https://educacao.uol.com.br/noticias/2019/06/01/mec-fica-isolado-apos-protestos-dizem-especialistas.htm"

t = myHtmlClass()
text = t.hml_cleaner(url)

f = fakenews()
dimension_language = f.check_language(url, text)
dimension_sentiment = f.check_sentiment(url, text)
dimension_key_words = f.check_key_words(url, text)

print(dimension_language)
print(dimension_sentiment)
print(dimension_key_words)
