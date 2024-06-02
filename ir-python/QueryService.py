from TextService import preprocess_text
from sklearn.metrics.pairwise import cosine_similarity


def search(
    query,
    documents,
    index,
    vectorizer,
    text_key,
    n=10,
    alpha=0.25,
):
    query_vec = vectorizer.transform([preprocess_text(query)])
    similarities = cosine_similarity(query_vec, index)[0]
    similarities_with_ids = [
        [item[0], item[1]] for item in zip(documents.index.to_list(), similarities)
    ]
    filtered_similarities_with_ids = [
        item for item in similarities_with_ids if item[1] > alpha
    ]
    sorted_similarities_with_ids = sorted(
        filtered_similarities_with_ids, key=lambda x: -x[1]
    )
    results = [
        {"id": item[0], "score": item[1], "text": documents.loc[item[0], text_key]}
        for item in sorted_similarities_with_ids
    ]

    return results
