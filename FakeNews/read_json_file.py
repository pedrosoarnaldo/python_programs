import json


json_file = open("/Users/arnaldo.pedroso/git/Monografia/news.json", "r", encoding="utf-8")

news = json.load(json_file)

for i in news:
  print(i["url"])

