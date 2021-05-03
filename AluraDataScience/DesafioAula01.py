import pandas as pd
import collections
import matplotlib.pyplot as plt

def count_frequency(my_list):
    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    data = collections.defaultdict(list)
    for key, value in freq.items():
        print("% s : % d" % (key, value))
        data[key].append(value)

    return data


movies = pd.read_csv('/Users/arnaldo.pedroso/PycharmProjects/python_programs/AluraDataScience/introducao-a-data-science/aula0/ml-latest-small/movies.csv')

'''Descobrindo Generos Unicos'''
genres = []
for i in movies["genres"]:
    genres.append(i)

genresClean = []
for i in genres:
    genresClean.append(str(i).split("|"))

#Limpar uma nested list exemplo
# [["Aventura", "Drama"], "Drama"]

finalGenres = []
for genres in genresClean:
    for category in genres:
        finalGenres.append(category)

genres = count_frequency(finalGenres)

pd.DataFrame.from_dict(genres, orient='index', columns=['count']).sort_values(by="count", ascending=False).plot(
    kind='bar',
    title='Filmes por categoria',
    figsize=(8, 8)
)

plt.show()
