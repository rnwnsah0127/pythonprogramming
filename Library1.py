from Books import Book

class Library:
    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)

    def showAllBooks(self):
        print("\n=== 전체 도서 목록 ===")
        for book in self.books:
            print(book.getInfo())

    def findByAuthor(self, author):
        print(f"\n=== '{author}' 저자의 도서 목록 ===")
        found = [b for b in self.books if b.author == author]
        if found:
            for book in found:
                print(book.getInfo())
        else:
            print("해당 저자의 책이 없습니다.")