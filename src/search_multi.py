import math

def read_query_file(file_path):
    """ Đọc file chứa danh sách từ khóa và trọng số """
    query_terms = {}
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                word, weight = parts[0].lower(), int(parts[1])
                query_terms[word] = weight
    return query_terms

def compute_idf(word, inverted_index, total_docs):
    """ Tính IDF cho nhiều từ khóa """
    df = len(inverted_index.get(word, {}))
    return math.log((total_docs + 1) / (df + 1))

def find_multi(word_file, N, inverted_index, doc_table):
    """ Tìm kiếm nhiều từ trong inverted index """
    query_terms = read_query_file(word_file)
    doc_scores = {}

    for word, weight in query_terms.items():
        if word in inverted_index:
            idf = compute_idf(word, inverted_index, len(doc_table))
            for doc_id, tf in inverted_index[word].items():
                doc_scores[doc_id] = doc_scores.get(doc_id, 0) + tf * weight * idf

    # Lấy top N tài liệu phù hợp nhất
    top_docs = sorted(doc_scores.items(), key=lambda x: x[1], reverse=True)[:N]

    return [(doc_table[doc_id], score) for doc_id, score in top_docs]
