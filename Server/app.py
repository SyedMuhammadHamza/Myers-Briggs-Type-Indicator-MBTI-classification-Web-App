# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 06:06:16 2021

@author: Syed Muhammmad Hamza
"""
from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
import string
import re
import numpy as np
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences
import nltk
nltk.download('stopwords')

#from gevent.pywsgi import WSGIServer
import keras as Keras
app = Flask(__name__)

def remove_URL(text):
    url = re.compile(r"https?://\S+|www\.\S+")
    return url.sub(r"", text)


def remove_html(text):
    html = re.compile(r"<.*?>")
    return html.sub(r"", text)
def remove_emoji(string):
    #unicode representation of emojis
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE,
    )
    return emoji_pattern.sub(r"", string)
def remove_punct(text):
    table = str.maketrans("", "", string.punctuation)
    return text.translate(table)
def remove_stopwords(text):
    text = [word.lower() for word in text.split() if word.lower() not in stop]

    return " ".join(text)
def predictmodel(sequence_padded):
        model = Keras.models.load_model("final_model.h5")
        prediction = model.predict(sequence_padded)
        #model._make_predict_function()
        return prediction


@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])

def predict():
    if request.method == 'POST':
        message = request.form['message'] 
        data = [message]
        print(data)
        print(type(data))
        text=" ".join(data)
        
        import nltk
        #stopwords=nltk.download('stopwords')
        #stop = set(stopwords.words("english"))
        text=remove_URL(text)
        text=remove_html(text)
        text=remove_emoji(text)
        text=remove_punct(text)
        nltk.download('stopwords')
        #text=remove_stopwords(text)
        x = pd.Series(text)
        
        x_sequence=tokenizer.texts_to_sequences(x)
        sequence_padded = pad_sequences(
             x_sequence, maxlen=150, padding="post", truncating="post"
        )
        Personality_Types_dict={0:'ISTJ',1:'infj',2:'intj',3:'enfj',4:'istp',5:'ESFJ',6:'infp',7:'ESFP',8:'ENFP',9:'estp',10:'ESTJ',11:'entj',12:'INTP',13:'isfj',14:'entp',15:'isfp'}
        '''
        global graph
        graph = tf.get_default_graph()
        with graph.as_default():
            prediction = model.predict(sequence_padded)
        '''
        prediction=predictmodel(sequence_padded)
        #prediction = model.predict(sequence_padded)
        print(prediction)
        pred=np.argmax(prediction)
        #result=Personality_Types_dict[int(pred)]
        result=pred
        print(result)

    return render_template('result.html',prediction = result)

if __name__ == '__main__':
    # loading tokenizer
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    app.run(port=5000)
    #app.run(host='0.0.0.0', port=5000)
    #app.run(debug=True)


 
