
import os
from collections import defaultdict


def find_multi(wordfile_path, N, inverted_index, doc_table):
    """
    Tìm kiếm nhiều từ từ một file chứa danh sách (word, weight).

    Parameters:
        wordfile_path (str): Đường dẫn đến file chứa truy vấn (mỗi dòng là "word weight").
        N (int): Số lượng tài liệu có điểm cao nhất cần trả về.
        inverted_index (dict): Dữ liệu inverted index: { term: {doc_id: tf, ...}, ... }
        doc_table (dict): Bảng ánh xạ doc_id → tên file.

    Returns:
        list of tuples: [(filename, total_score), ...] sắp xếp theo điểm giảm dần.
    """

    if not os.path.exists(wordfile_path):
        print(f"Lỗi: File '{wordfile_path}' không tồn tại.")
        return []

    scores = defaultdict(int)  # doc_id → tổng điểm

    with open(wordfile_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                word, weight_str = line.split()
                word = word.lower()
                weight = int(weight_str)
            except ValueError:
                print(f"Lỗi ở dòng {line_num}: '{line}' không đúng định dạng 'word weight'.")
                continue

            if word not in inverted_index:
                continue  # Từ không tồn tại trong index

            posting_list = inverted_index[word]  # dict: doc_id → tf

            for doc_id, tf in posting_list.items():
                scores[doc_id] += tf * weight

    # Sắp xếp các tài liệu theo điểm giảm dần
    top_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:N]
    results = [(doc_table[doc_id], score) for doc_id, score in top_docs]

    return results

