class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self. lendDict= {}

    def displayBooks(self):
        print(f"We have following in our library:, {self.name}")
        for book in self.booksList:
            print(book)

    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender book database has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")
    
    def addBook(self,book):
        self.booksList.append(book)
        print("Book has been added to the book list")

    def returnBook(self,book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    
    books = Library(['Python','Harry Potter','Rich Dad Poor Dad','C++ Basics','Algorithms by CLRS'],"Let's Upskill")

    while(True):
        print(f"Welcome to the {books.name} library. Enter Your Choice to continue.")
        print("1. Display books")
        print("2. Lend a book")
        print("3. Add a book")
        print("4. Return a book")
        user_choice = input("Enter your choice: ")

        if user_choice == '1':
            books.displayBooks()

        elif user_choice == '2':
            user = input("Enter your name: ")
            book = input("Enter book name: ")
            books.lendBook(user, book)

        elif user_choice == '3':
            book = input("Enter book name to add: ")
            books.addBook(book)

        elif user_choice == '4':
            book = input("Enter book name to return: ")
            books.returnBook(book)

        elif user_choice == '5':
            print("Thank you for using the library 📖")
            break

        else:
            print("Please enter a valid option")