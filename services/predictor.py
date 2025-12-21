import numpy as np
import os
import pickle

class PricePredictor:
    def __init__(self):
        model_path = os.path.join(os.path.dirname(__file__), '../artifacts/voting_regressor.pkl')
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)

    def predict(self, X):
        return self.model.predict(X)
    
predictor = PricePredictor()
