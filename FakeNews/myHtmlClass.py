from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re


class myHtmlClass:
    """This class is used to parse a html file and clean it converting to text."""

    def html_cleaner(self, url_to_be_analized):

        header = {
            'Content-Type': 'application/html; charset=UTF-8',
            'User-Agent': 'Mozilla/5.0'
        }

        try:
            html = Request(url_to_be_analized, headers=header)
            web_byte = urlopen(html).read()
            soup = BeautifulSoup(web_byte, "html.parser")

            # print(soup.body)

        except Exception as e:
            print(f"Error ----> {e}")
            exit(1)

        for script in soup.html(["script", "style"]):
            script.extract()  # rip it out

        text = soup.get_text()
        # print(f"{text}")

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())

        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("    "))

        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

        # limit text lenght
        # text = text[:5120]

        return text

    def prepare_text(self, text):

        h = myHtmlClass()
        hc = h.html_cleaner(text)

        pattern1 = '^[\w|\W]+\B[A-Z]+'
        pattern2 = '[a-z0-9á][A-Z]+[\w]+'

        final_list = []
        for i in hc.split('\n'):
            a = i.split()
            if len(a) > 35:
                l = []
                for z in i.split(' '):
                    if z != '':
                        z = z.replace("!", "")
                        l.append(z)
                        a = re.findall(pattern1, z)
                        # print(f"a--->{a} z--->{z}")
                        if (len(a) > 0) \
                                and (str(a[0]).replace("(", "").replace(")", "").replace("+", "") != z.replace("(",
                                                                                                               "").replace(
                            ")", "").replace("+", "")) \
                                and (z != "HQs"):
                            w = re.findall(pattern1, z)
                            y = re.findall(pattern2, z)

                            if len(y) == 0:
                                continue

                            w = w[0][:-1]
                            w = str(w)
                            # print(f"w--->{w}")
                            # print(f"y--->{y}")
                            y = y[0][1:]

                            l.remove(z)
                            l.append(w + str('.'))
                            l.append(y)
                for z in l:
                    final_list.append(z)

        final_string = ' '.join(final_list)
        return final_string
