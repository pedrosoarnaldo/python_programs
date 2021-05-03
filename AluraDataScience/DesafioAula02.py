import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


#Criar o boxplot dos 10 filmes com mais votos (não é com maior média, é com mais votos!).
# Não apenas plot mas também analise e tente tirar conclusões.

movies = pd.read_csv(
    '/Users/arnaldo.pedroso/PycharmProjects/python_programs/AluraDataScience/introducao-a-data-science/aula0/ml-latest-small/movies.csv'
)
rantings = pd.read_csv(
    '/Users/arnaldo.pedroso/PycharmProjects/python_programs/AluraDataScience/introducao-a-data-science/aula0/ml-latest-small/ratings.csv'
)


top_10_movies_by_rating = rantings.groupby("movieId").count()["rating"].sort_values(ascending=False).head(10)
total_ratings_for_top_10_movies = rantings.join(top_10_movies_by_rating, on="movieId", lsuffix="_r", rsuffix="_t", how="inner")

x = movies.merge(total_ratings_for_top_10_movies, on="movieId")

sb.boxplot(
    data=x,
    y=x["title"],
    x=x["rating_r"],
    orient="h",
)

plt.show()


#Criar um gráfico de notas médias por ano (média geral considerando todos os filmes lançados naquele ano).

