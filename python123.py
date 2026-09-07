class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    
    def getInfo(self):
        return f"제목:{self.title} 저자 : {self.author}  발행년도 : {self.year}"
    
class EBook(Book):
    def __init__(self,title,author,year,filesize):
        super().__init__(title,author,year)
        self.filesize = filesize

    def getInfo(self):
        base = super().getInfo()
        return f"{base}, 파일 사이즈 : {self.filesize}"
    
class PrintedBook(Book):
    def __init__(self, title, author, year,pages):
        super().__init__(title, author, year)
        self.pages = pages

    def getInfo(self):
        base = super().getInfo()
        return f"{base}, 페이지수 : {self.pages}"
    
