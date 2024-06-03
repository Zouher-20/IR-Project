from flask import Flask
from DatasetService import load_quora_docs, load_wiki_docs
from IndexingService import build_index, create_vectorizer
from QueryService import search
from flask import request

wiki_docs = load_wiki_docs()
wiki_vectorizer = create_vectorizer(wiki_docs["text_right"], "index-files/wiki-vec.pkl")
wiki_index = build_index(
    wiki_docs,
    "index-files/wiki.pkl",
    "text_right",
    wiki_vectorizer,
)

quora_docs = load_quora_docs()
quora_vectorizer = create_vectorizer(quora_docs["text"], "index-files/quora-vec.pkl")
quora_index = build_index(
    quora_docs,
    "index-files/quora.pkl",
    "text",
    quora_vectorizer,
)


app = Flask(__name__)


@app.route("/wiki")
def wiki_query():
    query = request.args.get("query", "")
    results = search(query, wiki_docs, wiki_index, wiki_vectorizer, "text_right")
    return results


@app.route("/quora")
def quora_query():
    query = request.args.get("query", "")
    results = search(query, quora_docs, quora_index, quora_vectorizer, "text")
    return results
