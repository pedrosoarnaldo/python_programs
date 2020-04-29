import pandas as pd
import matplotlib.pyplot as plt

vRatings = pd.read_csv('/Users/arnaldo.pedroso/PycharmProjects/python_programs/AluraDataScience/introducao-a-data-science/aula0/ml-latest-small/ratings.csv')
vMovies = pd.read_csv('/Users/arnaldo.pedroso/PycharmProjects/python_programs/AluraDataScience/introducao-a-data-science/aula0/ml-latest-small/movies.csv')

print("Shape do vRatings")
print(vRatings.shape)
print("")
print("vRatings.describe()")
print(vRatings.describe())
print("")
print("Quantidade de filmes com notas acima de 3.0")
print(len(vRatings.query("rating>3.0")))

print("")
print("Juntando os dados")
vAvgRatingsPerFilm = vRatings.groupby("movieId")["rating"].mean()
vCountRatingsPerFilm = vRatings.groupby("movieId")["rating"].count()

vJoin = vMovies.join(vAvgRatingsPerFilm, on="movieId").sort_values("rating", ascending=False)

'''Renomeando os campos para não dar erro de campo duplicado rating'''
vJoin.columns = ["movieId", "title", "genre", "avg_rating"]

vJoin1 = vJoin.join(vCountRatingsPerFilm, on="movieId").sort_values("avg_rating", ascending=False).values.tolist()

print("Title, avg_rating, count_rating")
for i in vJoin1:
    print(i[0], i[1], i[3], i[4])

print("")
print("Grafico")
vRatings.query("movieId == 312")["rating"].plot(kind='hist', title="Avaliações do Filme - Stuart Saves His Family (1995)")
plt.show()

# Descobrir os generos unicos dos filmes
vMovies["genres"].str.get_dummies('|').sum().sort_values(ascending=False).plot(
    kind='pie',
    title='Categorias de filmes e suas presenças relativas',
    figsize=(8, 8))
plt.show()

vMovies["genres"].str.get_dummies('|').sum().sort_values(ascending=False).plot(
    kind='bar',
    title='Filmes por categoria',
    figsize=(8,8))
plt.show()


