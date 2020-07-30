import ktrain
import pickle

class Predictor:
    def load_model(model_path):
        infile = open(model_path,'rb')
        model = pickle.load(infile)
        infile.close()
        return model

    def predict(model, data):
        response = model.predict(data)
        print(response)

#def load_model(predictor):
#    predictor = ktrain.load_predictor(predictor)
#    return predictor

#def predict(text):

x = Predictor.load_model('gs_mnb.p')
txt = "The camera is accessed via an app that runs on iOS or Android. Only the initial configuration needs to be done via wi-fi. After that, the app retains the camera's configuration and your mobile does not need to be on the local wi-fi."
Predictor.predict(x,txt)