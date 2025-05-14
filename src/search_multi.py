def find_multi(wordfile_path, N, inverted_index, doc_table):
    scores = {}

    with open(wordfile_path, 'r') as f:
        for line in f:
            word, weight = line.strip().split()
            word = word.lower()
            weight = int(weight)
            if word not in inverted_index:
                continue
            for doc_id, count in inverted_index[word].items():
                scores[doc_id] = scores.get(doc_id, 0) + count * weight

    top_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:N]
    return [(doc_table[doc_id], score) for doc_id, score in top_docs]
