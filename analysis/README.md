# Sentiment Analysis AI App

A beautiful and powerful sentiment analysis web application built with Flask and machine learning. This app analyzes text to determine whether the sentiment is positive or negative using advanced natural language processing techniques.

## Features

- **Beautiful UI**: Modern, responsive design with stunning gradients, animations, and smooth interactions
- **Real-time Analysis**: Instant sentiment prediction with confidence scores
- **Prediction History**: Keep track of all your analyses in a session-based history
- **Batch Processing**: API endpoint for analyzing multiple texts at once
- **Advanced Preprocessing**: Text cleaning, stopword removal, and stemming for better accuracy
- **Error Handling**: Robust error handling and user feedback
- **Mobile Responsive**: Works perfectly on all devices

## Technologies Used

- **Backend**: Flask (Python)
- **Machine Learning**: Scikit-learn, NLTK, TF-IDF Vectorization, Logistic Regression
- **Frontend**: HTML5, CSS3, JavaScript
- **Icons**: Font Awesome
- **Styling**: Modern CSS with gradients and animations

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sentiment-analysis-app.git
   cd sentiment-analysis-app/analysis
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Train the model:
   ```bash
   python train.py
   ```

4. Run the application:
   ```bash
   python main.py
   ```

5. Open your browser and go to `http://localhost:5000`

## Usage

1. Enter text in the textarea
2. Click "Analyze Sentiment" or press Enter
3. View the sentiment result with confidence score
4. Check your analysis history below
5. Clear text or history as needed

## API Endpoints

- `GET /`: Main application page
- `POST /predict`: Analyze single text sentiment
- `GET /history`: Get prediction history
- `POST /clear_history`: Clear prediction history
- `POST /batch_predict`: Analyze multiple texts (JSON)

## Model Training

The model is trained using:
- TF-IDF vectorization for text representation
- Logistic Regression classifier
- NLTK for text preprocessing (stopwords, stemming)
- Small dataset for demonstration (expand with your own data)

## Contributing

Feel free to contribute by:
- Adding more features
- Improving the UI/UX
- Enhancing the model accuracy
- Adding support for more languages

## License

This project is licensed under the MIT License - see the LICENSE file for details.
