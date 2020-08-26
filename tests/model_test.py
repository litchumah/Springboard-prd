from models.bert_loader import BertSentimentClassifier

def test_load_model():
    model = BertSentimentClassifier()
    assert model.__class__.__name__ == 'BertSentimentClassifier'
    

def test_model_prediction():
    model = BertSentimentClassifier()
    data="I've been buying AA and AAA batteries from Amazon Basics for a couple of years now. They recently changed the packaging (and presumably the manufacturer) and now they only last half as long. I tried a pair of Duracell AAs to test my hypothesis and they lasted almost three times as long. I wanted to stop buying these Amazon batteries, but it turns out that, at around $0.25 each and $0.90 for Duracell, they're still cheaper overall than buying name brand. However, it is extremely disappointing to watch them deliberately drop the quality and force us to purchase batteries more frequently. They've basically pulled a bait-and-switch with us, sucking us in with high quality batteries and then trading them out for lemons without dropping the price commensurately. Their packaging may be frustration-free, but these batteries sure aren't."
    assert model.predict(data) == 'bad'