import os
import re

def create_index(dir_path, stoplist_filename):
    inverted_index = {}
    doc_table = {}
    term_table = set()
    
    stoplist_path = os.path.join(dir_path, stoplist_filename)
    with open(stoplist_path, 'r') as f:
        stopwords = set(word.strip().lower() for word in f)

    for filename in os.listdir(dir_path):
        if filename == stoplist_filename:
            continue

        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r') as f:
            content = f.read()

        words = re.findall(r'\b\w+\b', content.lower())
        doc_id = len(doc_table)
        doc_table[doc_id] = filename

        for word in words:
            if word in stopwords or not word.startswith('c'):
                continue
            term_table.add(word)
            if word not in inverted_index:
                inverted_index[word] = {}
            if doc_id not in inverted_index[word]:
                inverted_index[word][doc_id] = 0
            inverted_index[word][doc_id] += 1

    return inverted_index, doc_table, term_table
