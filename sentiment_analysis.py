import ktrain
from ktrain import text
import pandas as pd
import tensorflow as tf

def is_there_any_gpu():
    if not tf.test.gpu_device_name():
        print('NO GPU FOUND')
    else:
        print('GPU: {}'.format(tf.test.gpu_device_name()))

def train_bert(data_frame):
    (x_train, y_train), (x_test, y_test), preproc = text.texts_from_df(df_merged, 
                                                                    'text',
                                                                    label_columns=['rating'],
                                                                    maxlen=50, 
                                                                    max_features=50,
                                                                    preprocess_mode='bert',
                                                                    val_pct=0.2,
                                                                    ngram_range=3)
    model = text.text_classifier('bert', (x_train, y_train) , preproc=preproc)
    learner = ktrain.get_learner(model, 
                                 train_data=(x_train, y_train), 
                                 val_data=(x_test, y_test), 
                                 batch_size=32)
    learner.fit_onecycle(2e-5, 1)
    predictor = ktrain.get_predictor(learner.model, preproc)
    predictor.save('sentiment_analysis')

def predict(predictor):
    predictor = ktrain.load_predictor(predictor)
