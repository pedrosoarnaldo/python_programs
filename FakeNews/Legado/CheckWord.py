import requests
# pprint is used to format the JSON response
from pprint import pprint
from IPython.display import HTML


subscription_key = "8b8eb83fb3ab4b3190bbfe6da37a3020"
text_analytics_base_url = "https://brazilsouth.api.cognitive.microsoft.com/text/analytics/v2.1/"


language_api_url = text_analytics_base_url + "languages"

documents = { "documents": [
    { "id": "1", "text": "This is a document written in English." },
    { "id": "2", "text": "Este es un document escrito en Español." },
    { "id": "3", "text": "这是一个用中文写的文件" }
]}

print("Validando linguas")
headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(language_api_url, headers=headers, json=documents)
languages = response.json()
pprint(languages)

sentiment_url = text_analytics_base_url + "sentiment"

documents = {"documents": [
  {"id": "1", "language": "en", "text": "I had a wonderful experience! The rooms were wonderful and the staff was helpful."},
  {"id": "2", "language": "en", "text": "I had a terrible time at the hotel. The staff was rude and the food was awful."},
  {"id": "3", "language": "es", "text": "Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos."},
  {"id": "4", "language": "es", "text": "La carretera estaba atascada. Había mucho tráfico el día de ayer."},
  {"id": "5", "language": "pt", "text": "Eu amo a minha esposa."}
]}

print("Validando sentimentos")
headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(sentiment_url, headers=headers, json=documents)
sentiments = response.json()
pprint(sentiments)

keyphrase_url = text_analytics_base_url + "keyPhrases"

documents = {"documents" : [
  {"id": "1", "language": "en", "text": "I had a wonderful experience! The rooms were wonderful and the staff was helpful."},
  {"id": "2", "language": "en", "text": "I had a terrible time at the hotel. The staff was rude and the food was awful."},
  {"id": "3", "language": "es", "text": "Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos."},
  {"id": "4", "language": "es", "text": "La carretera estaba atascada. Había mucho tráfico el día de ayer."},
  {"id": "5", "language": "pt", "text": "Hoje morreu Ayrton Senna da Silva."}
]}

print("palavras chave")
headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(keyphrase_url, headers=headers, json=documents)
key_phrases = response.json()
pprint(key_phrases)

entities_url = text_analytics_base_url + "entities"

documents = {"documents": [
  {"id": "1", "text": "Um dia um adeus e eu indo embora quanta loucura por tão pouca aventura."}
]}

print("Entidades")
headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(entities_url, headers=headers, json=documents)
entities = response.json()
pprint(entities)

