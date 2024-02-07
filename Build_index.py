import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from collections import defaultdict
from nltk.stem import SnowballStemmer
nltk.download('punkt')
nltk.download('stopwords')

def tokenize_titles(data, use_stemmer=False):
    french_stopwords = set(stopwords.words('french'))
    stemmer = SnowballStemmer("french") if use_stemmer else None
    
    # Preprocess and tokenize each title in the data
    titles = [item['title'] for item in data]
    tokenized_titles = []
    for title in titles:
        # Tokenization and lowercase conversion
        tokens = word_tokenize(title.lower(), language='french')
        # Remove punctuation and stopwords
        tokens = [token for token in tokens if token not in french_stopwords and token not in string.punctuation]
        # Apply stemming if requested
        if use_stemmer:
            tokens = [stemmer.stem(token) for token in tokens]
        tokenized_titles.append(tokens)
    return tokenized_titles

def inverted_index(data, use_stemmer=False):
    index = defaultdict(list)
    tokenized_titles = tokenize_titles(data, use_stemmer)
    
    for i, title_tokens in enumerate(tokenized_titles):
        for token in title_tokens:
            index[token].append(i)
    return index


def positional_index(data, use_stemmer=False):
    index = defaultdict(list)
    tokenized_titles = tokenize_titles(data, use_stemmer)
    
    for i, title_tokens in enumerate(tokenized_titles):
        for j, token in enumerate(title_tokens):
            index[token].append((i, j))  # Ajoute la position du token dans le titre
    return index