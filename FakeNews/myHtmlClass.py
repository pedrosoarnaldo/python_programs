from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


class myHtmlClass:
    """This class is used to parse a html file and clean it converting to text."""

    def html_cleaner(self, url_to_be_analized):

        html = Request(url_to_be_analized, headers={'User-Agent': 'Mozilla/5.0'})
        web_byte = urlopen(html).read()
        soup = BeautifulSoup(web_byte, "html.parser")

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
