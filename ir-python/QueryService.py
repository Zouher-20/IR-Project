from TextService import preprocess_text
from sklearn.metrics.pairwise import cosine_similarity


def search(query, dtm, vectorizer, document_ids, n=5, alpha=0.03):
    print(preprocess_text(query))
    query_vec = vectorizer.transform([preprocess_text(query)])
    similarities = cosine_similarity(query_vec, dtm)[0]
    relevant = [element for element in similarities if element >= alpha]

    document_ids_with_index = {i: element for i, element in enumerate(document_ids)}

    relevant_with_index = [(element, i) for i, element in enumerate(relevant)]

    sorted_similarities = sorted(relevant_with_index, key=lambda x: -x[0])

    top_n_results = []

    for i in range(n):
        if i > len(sorted_similarities) - 1:
            break
        if sorted_similarities[i][0] < alpha:
            break
        top_n_results.append(document_ids_with_index[sorted_similarities[i][1]])
    return top_n_results
