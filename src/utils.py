def print_top_documents(results):
    for filename, score in results:
        print(f"{filename}: {score}")
