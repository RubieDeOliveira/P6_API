import pickle

import numpy as np
import sklearn


class Model:

    def __init__(self):
        #Load model
        with open('resources/model.pickle', 'rb') as handle:
            self.model = pickle.load(handle)

        # Load vectorizer
        with open('resources/vectorizer.pickle', 'rb') as handle:
            self.vectorizer = pickle.load(handle)

        # Load y
        with open('resources/y.pickle', 'rb') as handle:
            self.y = pickle.load(handle)

    def predict_tags(self, data):
        vectors = self.vectorizer.transform([data])
        prediction = self.model.predict(vectors)
        columns_to_display = np.where(prediction == 1)
        tags = self.y.columns[columns_to_display[1]]
        return list(tags)
