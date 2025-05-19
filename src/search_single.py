import re
import math

class SingleSearch:
    def __init__(self, index):
        self.index = index  # index là từ điển dạng {word: {document: tf}}

    def normalize_word(self, word):
        """Chuẩn hóa từ: loại bỏ dấu câu, chữ thường hóa."""
        return re.sub(r'\W+', '', word).lower()

    def validate_input(self, word, weight):
        """Kiểm tra đầu vào hợp lệ."""
        if not isinstance(word, str) or not isinstance(weight, (int, float)):
            raise ValueError("Word phải là chuỗi và weight phải là số.")

    def compute_score(self, word, weight, doc_count):
        """Tính điểm dựa trên tf * weight, có thể thêm IDF nếu cần."""
        word = self.normalize_word(word)
        if word in self.index:
            tf_scores = self.index[word]
            scores = {
                doc: (tf * weight) * math.log(doc_count / (1 + len(tf_scores)))  # Thêm IDF
                for doc, tf in tf_scores.items()
            }
            return sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return []

# Ví dụ sử dụng:
index = {
    "computer": {"doc1.txt": 3, "doc2.txt": 5},
    "code": {"doc3.txt": 2, "doc1.txt": 1}
}
search = SingleSearch(index)
print(search.compute_score("computer", 2, 10))
