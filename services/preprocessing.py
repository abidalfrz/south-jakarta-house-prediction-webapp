import numpy as np
import pandas as pd
from sklearn.preprocessing import RobustScaler
from sklearn.feature_extraction.text import CountVectorizer
import re
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from nltk.tokenize import word_tokenize
import string
import pickle
import os

SCALER_PATH = os.path.join(os.path.dirname(__file__), '../artifacts/scaler.pkl')
VECTORIZER_PATH = os.path.join(os.path.dirname(__file__), '../artifacts/vectorizer.pkl')

def cleaning_nama_rumah(name):
    name = name.lower()
    STOPWORDS = set(StopWordRemoverFactory().get_stop_words())
    def remove_stopwords(text):
        tokens = word_tokenize(text)
        filtered_tokens = [word for word in tokens if word not in STOPWORDS]
        return ' '.join(filtered_tokens)
    name = remove_stopwords(name)
    name = re.sub(r'[^a-z0-9\s]', '', name)
    name = re.sub(rf'[{string.punctuation}]', ' ', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name

def add_features(df):
    df = df.copy()
    df['total_kamar'] = df['kamar_tidur'] + df['kamar_mandi']
    df['luas_bangunan_per_kamar_tidur'] = df['luas_bangunan'] / df['kamar_tidur']
    df['luas_bangunan_per_kamar_mandi'] = df['luas_bangunan'] / df['kamar_mandi']

    return df

def preprocess_data(df):
    df = df.copy()

    df['nama_rumah'] = df['nama_rumah'].apply(cleaning_nama_rumah)
    df = add_features(df)

    numeric = df.select_dtypes(include=[np.number]).columns.tolist()

    with open(SCALER_PATH, 'rb') as f:
        scaler = pickle.load(f)
    
    df_numeric = scaler.transform(df[numeric])

    with open(VECTORIZER_PATH, 'rb') as f:
        vectorizer = pickle.load(f)
    df_text = vectorizer.transform(df['nama_rumah']).toarray()

    X = np.hstack((df_numeric, df_text))
    return X

     



