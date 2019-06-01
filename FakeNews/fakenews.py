import requests
#from pprint import pprint
#from IPython.display import HTML

class fakenews:
    """This class analyze an url and says if the document is fakenews or not"""

    def __init__(self,
                 analitics_base_url="https://brazilsouth.api.cognitive.microsoft.com/text/analytics/v2.1/",
                 api="languages",
                 subscription_key="8b8eb83fb3ab4b3190bbfe6da37a3020"):

        self.analitics_base_url = analitics_base_url
        self.api = api
        self.subscrition_key = subscription_key
        self.headers = {"Ocp-Apim-Subscription-Key": subscription_key}

    ''' kill all scripts and style elements'''

    def check_language(self, url_to_be_analized, text):

        if self.api != "languages":
            api = "languages"
        else:
            api = self.api

        language_api_url = self.analitics_base_url + api
        documents = {"documents": [{ "id":"1", "text": text}]}

        response = requests.post(language_api_url, headers=self.headers, json=documents)
        languages = response.json()

        return languages

    def check_sentiment(self, url_to_be_analized, text):

        if self.api != "sentiment":
            api = "sentiment"
        else:
            api = self.api

        language_api_url = self.analitics_base_url + api

        documents = {"documents": [{"id": "1", "language": "pt", "text": text}]}

        response = requests.post(language_api_url, headers=self.headers, json=documents)
        sentiment = response.json()

        return sentiment

    def check_key_words(self, url_to_be_analized, text):

        if self.api != "entities":
            api = "entities"
        else:
            api = self.api

        language_api_url = self.analitics_base_url + api

        documents = {"documents": [{"id": "1", "text": text}]}

        response = requests.post(language_api_url, headers=self.headers, json=documents)
        key_words = response.json()

        return key_words
