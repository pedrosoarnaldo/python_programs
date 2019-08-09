class PoemClassifier:
    """Class used to count the number of poem syllables"""

    def linetoarray(phrase):
        return ' '.join(format(ord(x), 'b') for x in phrase)
