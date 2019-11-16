import DatabasePool as db
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from IPython.display import Image
import pydotplus
from io import StringIO
import collections

list_dimension = []
list_classification = []

### Creating database connection
dtb = db.DatabasePool()
d = dtb.connect_mongo()
database = d['fakenews']
url_collection = database['url']


# Load data
dict_colletion = url_collection.find({})
for i in dict_colletion:
    ld = [i["avg_entityTypeScore"], i["avg_wikipediaScore"], i["language_score"], i["sentiment_score"],
          i["total_entityTypeScore"], i["total_wikipediaScore"]]
    list_dimension.append(ld[:])
    list_classification.append(i["is_fake"])

data_feature_names = [ 'avg_entityTypeScore', 'avg_wikipediaScore', 'language_score', 'sentiment_score', 'total_entityTypeScore', 'total_wikipediaScore' ]

dtree=DecisionTreeClassifier()
dtree.fit(list_dimension, list_classification)

dot_data = StringIO()
export_graphviz(dtree,
                feature_names=data_feature_names,
                out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())

colors = ('turquoise', 'orange')
edges = collections.defaultdict(list)

for edge in graph.get_edge_list():
    edges[edge.get_source()].append(int(edge.get_destination()))

for edge in edges:
    edges[edge].sort()
    for i in range(2):
        dest = graph.get_node(str(edges[edge][i]))[0]
        dest.set_fillcolor(colors[i])

Image(graph.create_png())

# Create PDF
graph.write_pdf("/Users/arnaldo.pedroso/git/Monografia/fakenews_model.pdf")

# Create PNG
graph.write_png("/Users/arnaldo.pedroso/git/Monografia/fakenews_model.png")