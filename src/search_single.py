def find_single(word, weight, N, inverted_index, doc_table):
    word = word.lower()
    if word not in inverted_index:
        return []

    scores = {}
    for doc_id, count in inverted_index[word].items():
        scores[doc_id] = count * weight

    top_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:N]
    return [(doc_table[doc_id], score) for doc_id, score in top_docs]
