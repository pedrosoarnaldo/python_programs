import urllib.request
from bs4 import BeautifulSoup


class myHtmlClass:
    """This class is used to parse a html file and clean it converting to text."""

    def __init__(self,
                 url_to_be_analized="https://educacao.uol.com.br/noticias/2019/06/01/mec-fica-isolado-apos-protestos-dizem-especialistas.htm"):
        self.url_to_be_analized = url_to_be_analized

    def hml_cleaner(self, url_to_be_analized):

        if url_to_be_analized == '':
            url_to_be_analized = self.url_to_be_analized

        html = urllib.request.urlopen(url_to_be_analized)
        soup = BeautifulSoup(html, "html.parser")

        for script in soup(["script", "style"]):
            script.extract()    # rip it out

        # get text
        text = soup.get_text()

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())

        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

        # limit text lenght
        text = text[:5120]

        return text
