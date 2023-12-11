import tensorflow as tf
from tensorflow.keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from tensorflow import keras

import streamlit as st

import pickle
import pandas as pd

@st.cache_resource
def load_tokenizer():

    with open("models/lstm_token.pkl", "rb") as f:
        lstm_tokenizer = pickle.load(f)    

    return lstm_tokenizer

@st.cache_resource
def load_classifier():

    loaded_model = load_model("models/trained_lstm_model.h5", compile=False)

    return loaded_model 

def classify_tweets(tweet_text):

    model = load_classifier()
    tokenizer = load_tokenizer()


    encoded = pad_sequences(tokenizer.texts_to_sequences([tweet_text]), maxlen=100)

    result = model.predict(encoded)

    return result