
from flask import request, jsonify, render_template
from app import app
import joblib

from app.utils import preprocess_text


model = joblib.load("model/sentiment_model.pkl")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    text = request.form['text']
    processed_text = preprocess_text(text)
    prediction = model.predict([processed_text])[0]
    return jsonify({'prediction': prediction})
