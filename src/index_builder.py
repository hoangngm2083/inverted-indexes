import os
import re

def load_stopwords(stoplist_path):
    """ Đọc danh sách từ dừng từ tệp stoplist.txt """
    stopwords = set()
    with open(stoplist_path, 'r', encoding='utf-8') as f:
        stopwords = {line.strip().lower() for line in f}
    return stopwords

def create_index(directory, stoplist_path):
    """ Tạo Inverted Index từ các tệp trong thư mục """
    stopwords = load_stopwords(stoplist_path)
    inverted_index = {}
    doc_table = {}
    doc_id = 0

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if filename == "stoplist.txt" or not filename.endswith(".txt"):
            continue
        
        doc_id += 1
        doc_table[doc_id] = filename

        with open(file_path, 'r', encoding='utf-8') as f:
            words = re.findall(r'\b[cC]\w*\b', f.read().lower())  # Chỉ lấy từ bắt đầu bằng 'C'
        
        for word in words:
            if word not in stopwords:
                if word not in inverted_index:
                    inverted_index[word] = {}
                inverted_index[word][doc_id] = inverted_index[word].get(doc_id, 0) + 1

    return inverted_index, doc_table
