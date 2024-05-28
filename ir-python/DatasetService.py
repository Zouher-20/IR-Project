# Service to load datasets documents
import os
import pandas as pd


def load_wiki_docs():
    """
    Loads wiki dataset
    """

    path = "assets/wiki/documents.slice.csv"
    return pd.read_csv(path)
    # documents = {}

    # for index, row in data.iterrows():
    #     doc_id = row["id_right"]
    #     doc_content = row["text_right"]
    #     documents[doc_id] = doc_content

    # return documents


def lookup_doc(docs: pd.DataFrame, id, text_key):
    return docs.loc[id, text_key]  # Access text using label-based indexing


def load_quora_docs():
    """
    Loads quora dataset
    """

    path = "assets/quora/corpus.slice.jsonl"
    data = pd.read_json(path, lines=True)
    documents = {}

    for index, row in data.iterrows():
        doc_id = row["_id"]
        doc_content = row["text"]
        documents[doc_id] = doc_content

    return documents
