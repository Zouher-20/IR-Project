import os
from TextService import preprocess_text
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle


def create_vectorizer(data, vec_file):
    if os.path.exists(vec_file):
        loaded_vec = load_file(vec_file)
        return loaded_vec

    vectorizer = TfidfVectorizer(preprocessor=preprocess_text)
    vectorizer.fit(data)
    save_file(vectorizer, vec_file)
    return vectorizer


def build_index(documents, index_file, text_key, vectorizer):
    if os.path.exists(index_file):
        index = load_file(index_file)
        return index

    dtm = vectorizer.fit_transform(documents[text_key])
    save_file(dtm, index_file)
    return dtm


def save_file(index, index_file):
    with open(index_file, "wb") as f:
        pickle.dump(index, f)


def load_file(index_file):
    with open(index_file, "rb") as f:
        loaded_dtm = pickle.load(f)
        return loaded_dtm
