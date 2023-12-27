from urllib.parse import urlparse
import re
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pickle
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import re
import string



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
newsModel = load_model('fakeNewsModel.h5')
with open('preprocessed_data.pickle', 'rb') as f:
    _, _, tokenizer, maxlen = pickle.load(f)

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


def cleanForFakeNewsTest(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(f'[{re.escape(string.punctuation)}]', '', text) 
    text = re.sub(r'in', '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    text = text.replace('\n', ' ')
    return text

def classifyFakeNews(input_text):
    cleaned_text = cleanForFakeNewsTest(input_text)  # Use the clean_text function
    sequences = tokenizer.texts_to_sequences([cleaned_text])  # Tokenize text
    padded_sequences = pad_sequences(sequences, maxlen=maxlen)  # Pad sequences
    predictions = model.predict(padded_sequences)  # Make predictions