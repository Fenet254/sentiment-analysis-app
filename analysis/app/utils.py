

1aimport re

import nltk
from nltk.corpus import stopwords



from nltk.stem import PorterStemmer


# Download NLTK data if not present
nltk.download('stopwords', quiet=True)



def preprocess_text(text):

    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)


    words = text.split()
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]

    return ' '.join(words)
