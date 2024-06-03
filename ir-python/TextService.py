import re
import nltk
import contractions
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import PorterStemmer, WordNetLemmatizer
from textblob import TextBlob
from nltk.tokenize import word_tokenize


def preprocess_text(text):
    expanded = expand_contractions(text)
    cleaned_from_numbers = remove_numbers(expanded)
    typos_fixed = correct_typos(cleaned_from_numbers)
    punctioation_removed = clean_text(typos_fixed)
    tokenized_text = tokenize_text(punctioation_removed)
    stopwords_removed = remove_stopwords(tokenized_text)
    lemmatized_tokens = lemmatize_tokens(stopwords_removed)

    return " ".join(lemmatized_tokens)


def clean_text(text):
    cleaned_text = re.sub(r"[^\w\s]", "", text)
    return cleaned_text.lower()


def tokenize_text(text):
    tokens = word_tokenize(text)
    return tokens


def remove_stopwords(tokens):
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    return filtered_tokens


def lemmatize_tokens(tokens):
    lemmatizer = WordNetLemmatizer()
    tagged_tokens = nltk.pos_tag(tokens)
    lemmatized_tokens = []
    for token, tag in tagged_tokens:
        pos = get_wordnet_pos(tag)
        if pos:
            lemmatized_token = lemmatizer.lemmatize(token, pos=pos)
        else:
            lemmatized_token = lemmatizer.lemmatize(token)
        lemmatized_tokens.append(lemmatized_token)
    return lemmatized_tokens


def get_wordnet_pos(tag):
    if tag.startswith("N"):
        return nltk.corpus.wordnet.NOUN
    elif tag.startswith("V"):
        return nltk.corpus.wordnet.VERB
    elif tag.startswith("R"):
        return nltk.corpus.wordnet.ADV
    elif tag.startswith("J"):
        return nltk.corpus.wordnet.ADJ
    else:
        return None


def expand_contractions(text):
    expanded = contractions.fix(text)
    return expanded


def remove_numbers(text):
    return re.sub(r"\d+", "", text)


def correct_typos(text):
    textblob_obj = TextBlob(text)
    corrected_text = textblob_obj.correct()
    return str(corrected_text)
