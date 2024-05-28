import os
from TextService import preprocess_text
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pickle


def create_vectorizer():
    vectorizer = TfidfVectorizer(preprocessor=preprocess_text)
    return vectorizer


def build_index(documents, index_file, ids_file, text_key, ids_key, vectorizer):
    if os.path.exists(index_file):
        index = load_index(index_file)
        return index

    dtm = vectorizer.fit_transform(documents[text_key])

    document_ids = documents[ids_key].tolist()
    save_index(dtm, index_file)
    save_ids(ids_file, document_ids)
    return dtm


def save_index(index, index_file):
    with open(index_file, "wb") as f:
        pickle.dump(index, f)


def load_index(index_file):
    with open(index_file, "rb") as f:
        loaded_dtm = pickle.load(f)
        return loaded_dtm


def load_ids(ids_file):
    with open(ids_file, "rb") as f:
        document_ids = pickle.load(f)
        return document_ids


def save_ids(ids_file, document_ids):
    with open(ids_file, "wb") as f:
        pickle.dump(document_ids, f)
