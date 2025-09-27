class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.__pages = pages

    def setpages(self, pages):
        self.__pages = pages

    def getpages(self):
        return self.__pages
    
    def displayinfo(self):
        return self.__title, self.__author, self.__pages
        
b = Book("a","b",1)
print(b.displayinfo())
       