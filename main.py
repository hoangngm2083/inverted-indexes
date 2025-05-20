from src.index_builder import create_index
from src.search_single import find_single
from src.search_multi import find_multi
from src.utils import print_top_documents

# 1. Tạo index
index, doc_table, term_table = create_index('data', 'stoplist.txt')

while True:
    print("\nSelection search mode: ")
    print("0: exit")
    print("1: single search")
    print("2: multi search")
    
    try:
        search_mode = int(input("Enter your search mode: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if search_mode == 0: 
        print("Exiting...")
        break

    elif search_mode == 1:
        # 2. Tìm theo 1 từ
        word = input("Enter your search word: ").strip()
        try:
            weight = int(input("Enter your search word's weight: "))
        except ValueError:
            print("Invalid weight. Please enter a number.")
            continue

        print(f"\nTop documents for word='{word}' with weight='{weight}':")
        results = find_single(word, weight=weight, N=3, inverted_index=index, doc_table=doc_table)
        print_top_documents(results)

    elif search_mode == 2:
        # 3. Tìm theo nhiều từ
        print("\nTop documents for query from query_words.txt:")
        results = find_multi('data/query_words.txt', N=3, inverted_index=index, doc_table=doc_table)
        print_top_documents(results)

    else:
        print("Invalid mode. Please select 0, 1, or 2.")
