import nltk
from nltk.stem import SnowballStemmer, LancasterStemmer, PorterStemmer, RegexpStemmer, RSLPStemmer, WordNetLemmatizer
nltk.download('rslp')

# Phrases de test
phrases = [
    "Jouer",
    "joue",
    "jouais",
    "jouait",
    "jouerai",
    "jouerais",
    "joueuse",
    "joueur",
    "jouet",
    "jouir",
]

# Initialiser les stemmers/lemmatizers
snowball_stemmer = SnowballStemmer("french")
lancaster_stemmer = LancasterStemmer()
porter_stemmer = PorterStemmer()
regexp_stemmer = RegexpStemmer("ing$|s$")
rslp_stemmer = RSLPStemmer()

# Appliquer les stemmers/lemmatizers aux phrases de test
stemmers = {
    "SnowballStemmer": [snowball_stemmer.stem(word) for word in phrases],
    "LancasterStemmer": [lancaster_stemmer.stem(word) for word in phrases],
    "PorterStemmer": [porter_stemmer.stem(word) for word in phrases],
    "RegexpStemmer": [regexp_stemmer.stem(word) for word in phrases],
    "RSLPStemmer": [rslp_stemmer.stem(word) for word in phrases]
}

# Afficher les résultats
for stemmer, stemmed_phrases in stemmers.items():
    print(f"{stemmer}: {stemmed_phrases}")

# Selon ses exemples le meilleur est SnowballStemmer je vais l'utiliser dans le reste du travail 