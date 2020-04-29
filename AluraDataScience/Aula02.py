import pandas as pd
import matplotlib.pyplot as pl
import seaborn as sns

movies = pd.read_csv("/Users/arnaldo.pedroso/PycharmProjects/introducao-a-data-science/aula0/ml-latest-small/movies.csv")

genres = movies["genres"].str.get_dummies("|").sum().sort_values(ascending=False)

print(genres)
genres.plot(
    title="Filmes por categoria",
    kind='bar'
)

pl.show()

print(genres)
genres = movies["genres"].str.get_dummies("|").sum(axis=1).value_counts().plot(
    title="Generos por filmes",
    kind='bar'
)

pl.show()

sns.set_style("whitegrid")

genres = movies["genres"].str.get_dummies('|').sum().sort_values(ascending=False)
pl.figure(figsize=(16, 8))
sns.barplot(x=genres.index,
            y=genres.values,
            palette=sns.color_palette("BuGn_r", n_colors=len(genres) + 4)
            )
pl.show()

print(genres)
genres = movies["genres"].str.get_dummies("|").sum(axis=1).value_counts().plot.box()
pl.show()




