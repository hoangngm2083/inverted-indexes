
import math

def find_single(word, weight, N, inverted_index, doc_table):
    """Tìm tài liệu phù hợp với trọng số TF × weight × IDF."""
    word = word.lower()
    if word not in inverted_index:
        return []

    # Tính IDF để cân bằng từ phổ biến với từ hiếm
    total_docs = len(doc_table)
    doc_freq = len(inverted_index[word])
    idf = math.log((total_docs / (1 + doc_freq)))  # Tránh chia cho 0

    scores = {doc_id: (count * weight * idf) for doc_id, count in inverted_index[word].items()}

    top_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:N]
    return [(doc_table[doc_id], score) for doc_id, score in top_docs]
