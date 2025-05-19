import math

def validate_input(word, weight, N):
    """Kiểm tra đầu vào hợp lệ."""
    if not isinstance(word, str) or not isinstance(weight, (int, float)) or not isinstance(N, int):
        raise ValueError("Word phải là chuỗi, weight phải là số, N phải là số nguyên.")

def compute_idf(word, inverted_index, total_docs):
    """Tính IDF để cân bằng giữa từ phổ biến và hiếm."""
    if word in inverted_index:
        doc_freq = len(inverted_index[word])
        return math.log((total_docs / (1 + doc_freq)))  # Tránh chia cho 0
    return 0

def find_single(word, weight, N, inverted_index, doc_table, total_docs):
    """Tìm tài liệu phù hợp với trọng số TF × weight × IDF."""
    validate_input(word, weight, N)

    word = word.lower()
    if word not in inverted_index:
        return []

    idf = compute_idf(word, inverted_index, total_docs)
    scores = {
        doc_id: (count * weight * idf)  # Kết hợp IDF vào công thức tính điểm
        for doc_id, count in inverted_index[word].items()
    }

    top_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:N]
    return [(doc_table.get(doc_id, "Unknown"), score) for doc_id, score in top_docs]
