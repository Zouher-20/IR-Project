from flask import Flask
from DatasetService import load_quora_docs, load_wiki_docs, lookup_doc
from IndexingService import build_index, create_vectorizer, load_ids
from QueryService import search
from flask import request

wiki_docs = load_wiki_docs().set_index("id_right", drop=False)
wiki_vectorizer = create_vectorizer()
wiki_vectorizer.fit(wiki_docs["text_right"])
wiki_index = build_index(
    wiki_docs,
    "index-files/wiki.pkl",
    "index-files/wiki-ids.pkl",
    "text_right",
    "id_right",
    wiki_vectorizer,
)
wiki_ids = load_ids("index-files/wiki-ids.pkl")

# quora_docs = load_quora_docs()
# quora_index = build_index(quora_docs, "index-files/quora.txt")

app = Flask(__name__)


@app.route("/wiki")
def wiki_query():
    query = request.args.get("query", "")
    ids = search(query, wiki_index, wiki_vectorizer, wiki_ids)
    result = {id: lookup_doc(wiki_docs, id, "text_right") for i, id in enumerate(ids)}
    return result
