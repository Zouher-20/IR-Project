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


def evaluate_ir_system(qrels: dict, retrieved_documents: dict):
    average_precisions = {}

    for query_id, relevant_docs in qrels.items():
        precision_scores = {}
        recall_scores = {}
        retrieved_list = retrieved_documents.get(int(query_id), [])
        relevant_count = len(relevant_docs)

        retrieved_positions = {doc: i + 1 for i, doc in enumerate(retrieved_list)}

        true_positives = 0
        for i, doc in enumerate(retrieved_list):
            if str(doc) in relevant_docs:
                true_positives += 1
                precision = true_positives / (i + 1)
                recall = true_positives / relevant_count
                precision_scores[query_id, i + 1] = precision
                recall_scores[query_id, i + 1] = recall

        average_precisions[query_id] = sum(precision_scores.values()) / relevant_count

    mean_average_precision = sum(average_precisions.values()) / len(average_precisions)

    return {
        "precision": precision_scores,
        "recall": recall_scores,
        "average_precision": average_precisions,
        "mean_average_precision": mean_average_precision,
    }


def evaluate_ir_system2(qrels: dict, retrieved_documents: dict) -> float:
    """
    This function evaluates an information retrieval system and returns the mean average precision at cutoff 10 (MAP@10).

    Args:
        qrels: A dictionary mapping query IDs to lists of (document ID, relevance) tuples.
        retrieved_documents: A dictionary mapping query IDs to ranked lists of document IDs.

    Returns:
        The mean average precision at cutoff 10 (MAP@10).
    """
    precisions_at_10 = {}

    for query_id, relevant_docs in qrels.items():
        ap_num = 0
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
