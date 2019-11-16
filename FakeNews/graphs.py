import matplotlib.pyplot as plt
import DatabasePool as db

ldimension = ["avg_entityTypeScore", "avg_wikipediaScore", "language_score", "sentiment_score", "total_entityTypeScore", "total_wikipediaScore"]
ldimension_fake = []
ldimension_notfake = []

def read_dimension_data(dimension_name):
    dimension1 = []
    dimension2 = []

    ### Creating database connection
    dtb = db.DatabasePool()
    c = dtb.connect_mongo()
    database = c['fakenews']
    url_collection = database['url']

    for vis_fake in range(0, 2):
        c_url = url_collection.find({"is_fake": str(vis_fake)})
        if vis_fake == 0:
            for i in c_url:
                n = round(float(i[dimension_name]), 2)
                if n >= 1:
                    n = n/100
                dimension1.append(n)
        else:
            for i in c_url:
                n = round(float(i[dimension_name]), 2)
                if n >= 1:
                    n = n/100
                dimension2.append(n)

    ## closing database connection
    c.close()

    ## Analyzing data
    print('Dimension --->', dimension_name)
    print('Is not Fake --->', dimension1)
    print('Is fake --->', dimension2)

    return dimension1, dimension2


def format_graph(datagraph1, datagraph2, dimension):
    strdimension = 'Gráfico da Dimensão ' + dimension
    plt.rcParams.update({'font.size': 20})
    plt.figure(figsize=(8, 5))
    plt.scatter(datagraph1, datagraph1, color='b', s=200, alpha=0.60)
    plt.scatter(datagraph2, datagraph2, color='r', s=200, alpha=0.60)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.xticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    plt.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(strdimension)
    plt.grid(True)
    plt.show()


# Dimensions
# "avg_entityTypeScore"
# "avg_wikipediaScore"
# "language_score"
# "sentiment_score"
# "total_entityTypeScore"
# "total_wikipediaScore"

for d in ldimension:
    ldimension_fake, ldimension_notfake = read_dimension_data(d)
    format_graph(ldimension_fake, ldimension_notfake, d)
    del ldimension_fake[:]
    del ldimension_notfake[:]
