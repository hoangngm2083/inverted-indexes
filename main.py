from src.index_builder import create_index
from src.search_single import find_single
from src.search_multi import find_multi
from src.utils import print_top_documents

# 1. Tạo index
index, doc_table, term_table = create_index('data', 'stoplist.txt')

print("index",index)
print("doc_table",doc_table)
print("term_table",term_table)

# 2. Tìm theo 1 từ
print("Top documents for word='cat':")
results = find_single('cat', weight=3, N=3, inverted_index=index, doc_table=doc_table)
print_top_documents(results)

# 3. Tìm theo nhiều từ
print("\nTop documents for query from file:")
results = find_multi('data/query_words.txt', N=3, inverted_index=index, doc_table=doc_table)
print_top_documents(results)
