from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        tag = str(tag).lower()
        if tag == 'author':
            print("Encountered a start tag:", tag)


parser = MyHTMLParser()
parser.feed('<meta name="author" content="John Doe">')