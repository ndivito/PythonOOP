class Library:
    def __init__(self,booklist):
        self.booklist = booklist

    def displayAvBooks(self):
        for book in self.booklist:
            print(book)
    def lendBook(self, requestedBook):
        if requestedBook in self.booklist:
            print("you have the book ", requestedBook)
        else:
            print('no such book')
    def addBook(self, returnBook):
        self.booklist.append(returnBook)
        print('thanks for returning ', returnBook)


class Customer:
    def requestBook(self):
        print("Enter the name of the book you want to borrow")
        self.book = input()
        return self.book
    def returnBook(self):
        print('enter the name of the book you are returning')
        self.book = input()
        return self.book

library = Library(['b1', 'b2', 'b3'])
customer = Customer()
while True:
    print('1 display, 2 request, 3 return, 4 exit')
    userchoice = int(input())
    if userchoice == 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userchoice == 3:
        returnBook = customer.returnBook()
        library.addBook(returnBook)
    elif userchoice == 4:
        quit()
    elif userchoice == 1:
        library.displayAvBooks()