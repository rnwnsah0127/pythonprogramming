from datetime import date
from CustomException import *

class Member:
    def __init__(self, member_id, name, phone):
        self.member_id = member_id
        self.name = name
        self.phone = phone
        self.borrowed_books = {}   # {isbn: 대출일(date)}

    def borrow(self, isbn):
        if isbn in self.borrowed_books:
            raise AlreadyBorrowedBookException('이미 대출 중인 도서입니다.')
        self.borrowed_books[isbn] = date.today()

    def return_book(self, isbn):
        if isbn not in self.borrowed_books:
            raise NoBookException('대출 기록이 없는 도서입니다.')
        return self.borrowed_books.pop(isbn)   # 대출일 반환