import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np

movies = pd.read_csv('/Users/arnaldo.pedroso/PycharmProjects/python_programs/AluraDataScience/introducao-a-data-science/aula0/ml-latest-small/movies.csv')

x = movies[["movieId", "title"]]
x = x.values.tolist()

movie = []

for i in x:
    movieId = i[0]
    title = i[1]
    year = re.findall(" \([0-9]+\)", str(i[1]))
    year = re.findall('\d+', str(year))
    if len(year) == 1:
        year = int(year[0])
    else:
        year = ''
    movie.append([movieId, title, year])

df = pd.DataFrame(movie)
df.columns = ["movieId", 'title', 'year']

df.groupby("year").count()["movieId"].plot(
    kind="bar"
)

plt.title("Filmes avaliados - Por ano de Lançamento do Filme")
plt.xticks(rotation=45)
plt.show()

ratings = pd.read_csv('/Users/arnaldo.pedroso/PycharmProjects/python_programs/AluraDataScience/introducao-a-data-science/aula0/ml-latest-small/ratings.csv')


### Variância
print("")
print("Variância")
print(np.var(ratings["rating"]))

### Desvio padrão das notas
print("")
print("Desvio Padrão")
print(np.std(ratings["rating"]))

### média
print("")
print("Média")
print(np.mean(ratings["rating"]))

### mediana
print("")
print("Mediana")
print(np.median(ratings["rating"]))

### describe
print("")
print(ratings["rating"].describe())

