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


def evaluate_ir_system(qrels: dict, retrieved_documents: dict) -> float:
    precisions_at_10 = {}

    for query_id, relevant_docs in qrels.items():
        retrieved_list = retrieved_documents.get(int(query_id), [])
        if len(retrieved_list) >= 10:
            relevant_at_10 = [
                doc for doc in retrieved_list[:10] if str(doc) in relevant_docs
            ]
            precision_at_10 = len(relevant_at_10) / 10
        else:
            precision_at_10 = 0

        precisions_at_10[query_id] = precision_at_10

    mean_average_precision_at_10 = sum(precisions_at_10.values()) / len(
        precisions_at_10
    )

    return mean_average_precision_at_10
