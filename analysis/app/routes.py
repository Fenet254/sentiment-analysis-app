



from flask import request, jsonify, render_template, session, flash
from flask_cors import CORS
from app import app
import joblib
import logging


from app.utils import preprocess_text



# Enable CORS for Next.js frontend



CORS(app)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


model = joblib.load("model/sentiment_model.pkl")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    try:
        text = request.form.get('text', '').strip()
        if not text:
            return jsonify({'error': 'No text provided'}), 400

        processed_text = preprocess_text(text)
        prediction = model.predict([processed_text])[0]
        confidence = max(model.predict_proba([processed_text])[0])

        # Store in session history
        if 'history' not in session:
            session['history'] = []
        session['history'].append({'text': text, 'prediction': prediction, 'confidence': round(confidence * 100, 2)})
        session.modified = True

        logger.info(f"Prediction made for text: '{text}' -> {prediction}")
        return jsonify({'prediction': prediction, 'confidence': round(confidence * 100, 2)})
    except Exception as e:
        logger.error(f"Error in prediction: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/history', methods=['GET'])
def get_history():
    history = session.get('history', [])
    return jsonify({'history': history})

@app.route('/clear_history', methods=['POST'])
def clear_history():
    session['history'] = []
    session.modified = True
    return jsonify({'message': 'History cleared'})

@app.route('/batch_predict', methods=['POST'])
def batch_predict():
    try:
        texts = request.json.get('texts', [])
        if not texts or not isinstance(texts, list):
            return jsonify({'error': 'Invalid input: expected list of texts'}), 400

        processed_texts = [preprocess_text(text) for text in texts]
        predictions = model.predict(processed_texts).tolist()
        confidences = [round(max(proba) * 100, 2) for proba in model.predict_proba(processed_texts)]

        results = [{'text': text, 'prediction': pred, 'confidence': conf} for text, pred, conf in zip(texts, predictions, confidences)]
        return jsonify({'results': results})
    except Exception as e:
        logger.error(f"Error in batch prediction: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500
