class Book:
    def __init__(self, title, author, isbn, total_copies=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = total_copies  # 대출 가능 권수

    def is_available(self):
        return self.available_copies > 0      # 대출 가능 여부

    def __str__(self):
        status = '대출 가능' if self.is_available() else '대출 중'
        return f'[{self.isbn}] {self.title} - {self.author} ({self.available_copies}/{self.total_copies}권) [{status}]'
