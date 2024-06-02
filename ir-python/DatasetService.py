import pandas as pd


def load_wiki_docs():
    path = "assets/wiki/documents.csv"
    return pd.read_csv(path).set_index("id_right", drop=False)


def load_quora_docs():
    path = "assets/quora/corpus.jsonl"
    return pd.read_json(path, lines=True).set_index("_id", drop=False)


def load_wiki_qrels(qrels_file="assets/wiki/training/qrels"):
    qrels = {}
    with open(qrels_file, "r", encoding="utf-8") as f:
        for line in f:
            qid, _, docid, relevance = line.strip().split("\t")
            qrels.setdefault(qid, []).append(docid)
    return qrels


def load_quora_qrels(qrels_file="assets/quora/qrels/dev.tsv"):
    qrels = {}
    i = 0
    with open(qrels_file, "r", encoding="utf-8") as f:
        for line in f:
            if i == 0:
                i += 1
                continue
            i += 1
            qid, docid, relevance = line.strip().split("\t")
            qrels.setdefault(qid, []).append(docid)
    return qrels


def load_wiki_queries(queries_file="assets/wiki/training/queries.csv"):
    return pd.read_csv(queries_file).set_index("id_left", drop=False)


def load_quora_queries(queries_file="assets/quora/queries.jsonl"):
    return pd.read_json(queries_file, lines=True).set_index("_id", drop=False)
