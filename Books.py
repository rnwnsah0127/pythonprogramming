# book.py

class Book:
    def __init__(self, title, author, year):
        self.title  = title
        self.author = author
        self.year   = year

    def getInfo(self):
        return f"제목: {self.title}, 저자: {self.author}, 년도: {self.year}"


class Ebook(Book):
    def __init__(self, title, author, year, fileSize):
        super().__init__(title, author, year)
        self.fileSize = fileSize

    def getInfo(self):
        base = super().getInfo()
        return f"{base}, 파일 크기: {self.fileSize}MB"


class PrintedBook(Book):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages

    def getInfo(self):
        base = super().getInfo()
        return f"{base}, 페이지 수: {self.pages}"