from urllib.parse import urlparse
import re
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pickle


def get_domain_name(url: str) -> str:
    if not url.startswith('http'):
        url = 'http://' + url
    parsed_url = urlparse(url)
    domain_name = "{uri.netloc}".format(uri=parsed_url)
    return domain_name

# LOAD THE MODEL AND VECTORIZER
with open('reviewModel.pkl', 'rb') as f:
    model = pickle.load(f)
with open('reviewVecotorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# FOR NLTK
# nltk.download('stopwords')

# TEXT PREPROCESSING
sw = set(stopwords.words('english'))

def text_preprocessing(text):
    txt = TextBlob(text)
    result = txt.correct()
    removed_special_characters = re.sub("[^a-zA-Z]", " ", str(result))
    tokens = removed_special_characters.lower().split()
    stemmer = PorterStemmer()

    cleaned = []
    stemmed = []

    for token in tokens:
        if token not in sw:
            cleaned.append(token)

    for token in cleaned:
        token = stemmer.stem(token)
        stemmed.append(token)

    return " ".join(stemmed)

def reviewTester(text):

    cleaned_review = text_preprocessing(text)
    sequence = vectorizer.transform([cleaned_review])
    prediction = model.predict(sequence)

    return prediction[0]