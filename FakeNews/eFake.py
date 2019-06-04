from sklearn import tree
from DatabasePool import DatabasePool


class fakenews():
    """This class is responsible to verify if an url is fake or not"""

    def load_tree(self):

        list_dimension = []
        list_classification = []
        d = DatabasePool()
        c = d.connect_mongo()

        database = c['fakenews']
        url_collection = database['url']

        dict_colletion = url_collection.find({})
        for i in dict_colletion:
            ld = [i["avg_entityTypeScore"], i["avg_wikipediaScore"], i["language_score"], i["sentiment_score"], i["total_entityTypeScore"], i["total_wikipediaScore"]]
            list_dimension.append(ld[:])
            list_classification.append(i["is_fake"])

        return list_dimension, list_classification

    def classify_url(self, dimension):
        ld, lc = self.load_tree()

        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(ld, lc)

        return clf.predict([dimension])
