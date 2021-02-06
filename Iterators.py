class Book:
    def __init__(self,name,cost,author):
        self.name = name
        self.cost = cost
        self.author = author
    def __str__(self):
        return "Name: " + self.name + " ; Cost: " + self.cost + "; Author:" + self.author
    def __repr__(self):
        return "Name: " + self.name + " ; Cost: " + self.cost + " ; Author:" + self.author
class BackPack:
    def __init__(self,books):
        self.books = books
    def __str__(self):
        return books.__str()
    def __repr__(self):
        return books.__str()

    def __iter__(self):
        self.iterator = 0
        return self
    def __next__(self):
        if(self.iterator < len(self.books)):
            book_now = self.books[self.iterator]
            self.iterator = self.iterator + 1
            return book_now
        else:
            raise StopIteration

b1 = Book("Fountain Head", "$35","Ayn Rand")  
b2 = Book("The Daughter's Tale", "$20" ,"Armanda")
b3 = Book("Himself", "$45" ,"Jess")

books_list = [b1,b2,b3]
bpack1 = BackPack(books_list)
print("--> Calling internal iterator")
for iterator in bpack1:
    print(iterator)
""" iterator_x = iter(bpack1)
print("--> Calling explit iterator")
print(next(iterator_x))
print(next(iterator_x))
print(next(iterator_x))
 """