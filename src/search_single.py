import math

def compute_idf(word, inverted_index, total_docs):
    """ Tính IDF cho một từ """
    df = len(inverted_index.get(word, {}))  # Số tài liệu chứa từ đó
    return math.log((total_docs + 1) / (df + 1))  # +1 để tránh lỗi chia cho 0

def find_single(word, weight, N, inverted_index, doc_table):
    """ Tìm kiếm đơn với IDF """
    word = word.lower()

    if word not in inverted_index:
        return []

    idf = compute_idf(word, inverted_index, len(doc_table))
    doc_scores = {}

    for doc_id, tf in inverted_index[word].items():
        doc_scores[doc_id] = tf * weight * idf  # Áp dụng IDF vào tính điểm

    # Sắp xếp theo điểm số giảm dần
    top_docs = sorted(doc_scores.items(), key=lambda x: x[1], reverse=True)[:N]
    
    return [(doc_table[doc_id], score) for doc_id, score in top_docs]
