from CustomException import *
from Book import Book
from Member import Member

class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}    # {isbn: Book 객체}
        self.members = {} # {member_id: Member 객체}

    def add_book(self, title, author, isbn, total_copies=1):
        if isbn in self.books:                         # 이미 있으면 권수만 추가
            self.books[isbn].total_copies += total_copies
            self.books[isbn].available_copies += total_copies
        else:
            self.books[isbn] = Book(title, author, isbn, total_copies)
        print(f'도서 추가 완료: {self.books[isbn]}')

    def register_member(self, member_id, name, phone):
        if member_id in self.members:
            raise UserExistException('이미 등록된 회원 번호입니다.')
        self.members[member_id] = Member(member_id, name, phone)

    # ── 검색 (Library 클래스 내부) ──
    def search_books(self, keyword, search_type='title'):
        if search_type == 'title':
            results = [b for b in self.books.values() if keyword.lower() in b.title.lower()]
        else:  # 'author'
            results = [b for b in self.books.values() if keyword.lower() in b.author.lower()]
        for b in results:
            print(f'  {b}')
        if not results:
            print('검색 결과가 없습니다.')

    # ── 대출 ──
    def borrow_book(self, member_id, isbn):
        if member_id not in self.members:
            raise NoExistMemberException('등록되지 않은 회원입니다.')
        if isbn not in self.books:
            raise NoExistBookException('등록되지 않은 도서입니다.')
        if not self.books[isbn].is_available():
            raise NotEnoughBookException('대출 가능 권수가 없습니다.')
        self.members[member_id].borrow(isbn)
        self.books[isbn].available_copies -= 1
        print(f'대출 완료: {self.members[member_id].name} → {self.books[isbn].title}')

    # ── 반납 ──
    def return_book(self, member_id, isbn):
        if member_id not in self.members:
            raise NoExistMemberException('등록되지 않은 회원입니다.')
        if isbn not in self.books:
            raise NoExistBookException('등록되지 않은 도서입니다.')
        self.members[member_id].return_book(isbn)
        self.books[isbn].available_copies += 1
        print(f'반납 완료: {self.members[member_id].name} → {self.books[isbn].title}')

    def show_all_books(self):
        if not self.books:
            print('등록된 도서가 없습니다.')
            return

        print('\n[전체 도서 목록]')
        for book in self.books.values():
            print(book)
 