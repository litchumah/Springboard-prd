from ktrain import load_predictor


class BertSentimentClassifier():
    def __init__(self):
        self.model = load_predictor('/Users/litchisunzulato/Desktop/fu/bert')

    def predict(self, data):
        return self.model.predict(data)