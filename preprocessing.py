import pandas as pd
import unicodedata
import contractions
import re
from gensim.parsing.preprocessing import strip_multiple_whitespaces
from nltk import download, data
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer

class Preprocessing:

    def good_bad_neutral(number):
        if number > 3:
            return 'good'
        elif number == 3:
            return 'neutral'
        else:
            return 'bad'

    def load_and_preprocess(csv_file_path):
        try:
            data.find('tokenizers/punkt.zip')
        except LookupError:
            download('punkt')
        try:
            data.find('tokenizers/stopwords.zip')
        except LookupError:
            download('stopwords')
        df = pd.read_csv(csv_file_path, names=['rating','title','text'])
        df = df[['rating','text']]
        pattern = r'[^a-zA-Z\s]'
        stop_words = set(stopwords.words('english'))
        porter = PorterStemmer()
        df['text'] = df['text'].apply(lambda x: unicodedata.normalize('NFKD', x).encode('ascii', 'ignore').decode('utf-8', 'ignore'))
        df['text'] = df['text'].apply(lambda x: contractions.fix(x))
        df['text'] = df['text'].apply(lambda x:re.sub(pattern, '', x))
        df['text'] = df['text'].apply(lambda x: x.lower())
        df['text'] = df['text'].apply(lambda x: strip_multiple_whitespaces(x))
        df.rating = df['rating'].apply(lambda x: Preprocessing.good_bad_neutral(x))
        df['text'] = df['text'].apply(lambda x: word_tokenize(x))
        df['text'] = df['text'].apply(lambda x: [word for word in x if word not in stop_words])
        df['text'] = df['text'].apply(lambda x: [porter.stem(word) for word in x])
        df['text'] = df['text'].apply(lambda x: ' '.join(x))
        df = df[df['text'].notna()]
        return df

Preprocessing.load_and_preprocess('test.csv')