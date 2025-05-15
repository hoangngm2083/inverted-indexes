import os
import re
from collections import defaultdict

def create_index(dir_path, stoplist_filename):
    inverted_index = defaultdict(dict)
    doc_table = {}
    
    # Đọc stoplist
    stoplist_path = os.path.join(dir_path, stoplist_filename)
    with open(stoplist_path, 'r') as f:
        stopwords = set(f.read().splitlines())

    # Liệt kê tệp bằng os.scandir
    doc_id = 0
    for entry in os.scandir(dir_path):
        if entry.name == stoplist_filename or not entry.is_file():
            continue

        # Đọc tệp theo dòng
        filepath = entry.path
        with open(filepath, 'r') as f:
            doc_table[doc_id] = entry.name
            for line in f:
                words = re.findall(r'\b\w+\b', line.lower())
                for word in words:
                    if not word.startswith('c') or word in stopwords:
                        continue
                    inverted_index[word][doc_id] = inverted_index[word].get(doc_id, 0) + 1
        doc_id += 1

    return dict(inverted_index), doc_table, set(inverted_index.keys())