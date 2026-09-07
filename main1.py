from Library1 import Library
from Books import Ebook, PrintedBook

library = Library()

for i in range(5):
    print(f"\n {i+1}번째 책")
    bookType = input("printed or ebook 입력").strip()
    title = input("제목 입력 : ").strip()
    author = input("저자 입력 : ").strip()
    year = int(input("발행 년도 입력 : ")).strip

    if bookType == "printed":
        pages = int(input("페이지 수 입력 : "))
        book = PrintedBook(title,author,year,pages)
    else:
        filesize = float(input("파일 사이즈 입력"))
        book = Ebook(title,author,year,filesize)

    library.addBook(book)
library.showAllBooks()

searchAuthor = input("\n검색할 저자 입력 : ")
library.findByAuthor(searchAuthor)