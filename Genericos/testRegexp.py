import re

string = '_Copyright'
string1 = 'meta:name="Copyright"'


if re.search('copyright', string1.lower()):
    print('Match')
else:
    print('no match')