import numpy as np
import os
import pickle

class PricePredictor:
    def __init__(self):
        model_path = os.path.join(os.path.dirname(__file__), '../artifacts/voting_regressor.pkl')
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)

    def predict(self, X):
        pred = self.model.predict(X)
        return np.expm1(pred)  # Inverse of log1p transformation
    
predictor = PricePredictor()
