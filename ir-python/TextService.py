import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import PorterStemmer


def preprocess_text(text):
    stop_words = stopwords.words("english")

    stemmer = PorterStemmer()

    tokens = []
    for word in re.findall(r"(?:" + r"|\S+)", text):
        tokens.append(clean_token(word))

    processed_tokens = []
    for token in tokens:
        token = token.lower()
        token = re.sub(r"\d", "", token)

        if any(c.isalpha() for c in token):
            if len(token) > 2:
                stemmed_token = stemmer.stem(token)
                if stemmed_token not in stop_words:
                    processed_tokens.append(stemmed_token)

    return " ".join(processed_tokens)


def clean_token(token):
    return re.sub(r"[^a-zA-Z0-9]", "", token)
