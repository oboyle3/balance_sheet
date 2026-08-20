

#think of a class like a blueprint. The class describes what the book is.
#for example
#Book
# |
# | -> title 
# | -> author
# | -> pages
class Book:
    def __init__(self, title, author): # __init__() runs when we create a object
        self.title = title
        self.author = author 