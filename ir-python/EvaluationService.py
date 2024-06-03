import os
from QueryService import search
from IndexingService import load_file, save_file
from sklearn.metrics import average_precision_score


def get_queries_results(
    queries,
    docs,
    index,
    vectorizer,
    documents_text_key,
    queries_text_key,
    queries_id_key,
    results_file,
):
    if os.path.exists(results_file):
        retrieved = load_file(results_file)
        return retrieved

    retrieved = {}
    for ind in queries.index:
        query_results = search(
            queries[queries_text_key][ind], docs, index, vectorizer, documents_text_key
        )
        for item in query_results:
            retrieved.setdefault(queries[queries_id_key][ind], []).append(item["id"])
    save_file(retrieved, results_file)
    return retrieved


def evaluate_ir_system(qrels: dict, retrieved_documents: dict, k=10) -> dict:
    metrics = {"map": 0, "recall_at_k": [], "mrr": 0}

    precisions_at_k = {}
    for query_id, relevant_docs in qrels.items():
        retrieved_list = retrieved_documents.get(int(query_id), [])
        relevant_at_k = [doc for doc in retrieved_list[:k] if str(doc) in relevant_docs]
        actual_k = min(k, len(retrieved_list))
        if actual_k != 0:
            precision_at_k = len(relevant_at_k) / k
            reciprocals = [
                1 / (i + 1)
                for i, doc in enumerate(retrieved_list)
                if str(doc) in relevant_docs
            ]
        else:
            precision_at_k = 0
            reciprocals = []

        precisions_at_k[query_id] = precision_at_k
        metrics["mrr"] += sum(reciprocals) if reciprocals else 0

        recall_at_k = len(relevant_at_k) / min(k, len(relevant_docs))
        metrics["recall_at_k"].append((query_id, recall_at_k))

    metrics["map"] = sum(precisions_at_k.values()) / len(precisions_at_k)
    metrics["mrr"] /= len(qrels)

    return metrics
