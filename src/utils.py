def print_top_documents(results):
    if not results:
        print("Không tìm thấy tài liệu phù hợp.")
        return
    for filename, score in results:
        print(f"{filename}: {score}")
