class Author:
    all = []

    def __init__(self, name):
        self._name = name
        Author.all.append(self)

    def get_name(self):
        return self._name

    def set_name(self, value):
        if type(value) is str:
            self._name = value
        else:
            raise Exception("Name must be string")

    name = property(get_name, set_name)

    def contracts(self):
        returnList = list()
        for contract in Contract.all:
            if contract.author is self:
                returnList.append(contract)
        return returnList

    def books(self):
        returnList = list()
        for contract in Contract.all:
            if contract.author is self:
                returnList.append(contract.book)
        return returnList

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        returnList = list()
        for contract in Contract.all:
            if contract.author is self:
                print(contract.royalties)
                returnList.append(contract.royalties)
        return sum(returnList)


class Book:
    all = []

    def __init__(self, title):
        self._title = title
        Book.all.append(self)

    def get_title(self):
        return self._title

    def set_title(self, value):
        if type(value) is str:
            self._title = value
        else:
            raise Exception("Title must be string")

    title = property(get_title, set_title)

    def contracts(self):
        returnList = list()
        for contract in Contract.all:
            if contract.book is self:
                returnList.append(contract)
        return returnList

    def authors(self):
        returnList = list()
        for contract in Contract.all:
            if contract.book is self:
                returnList.append(contract.author)
        return returnList


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    def get_author(self):
        return self._author

    def set_author(self, value):
        if type(value) is Author:
            self._author = value
        else:
            raise Exception("Author must be of type Author")

    author = property(get_author, set_author)

    def get_book(self):
        return self._book

    def set_book(self, value):
        if type(value) is Book:
            self._book = value
        else:
            raise Exception("Book must be of type Book")

    book = property(get_book, set_book)

    def get_date(self):
        return self._date

    def set_date(self, value):
        if type(value) is str:
            self._date = value
        else:
            raise Exception("Date must be of type string")

    date = property(get_date, set_date)

    def get_royalities(self):
        return self._royalties

    def set_royalties(self, value):
        if type(value) is float or type(value) is int:
            self._royalties = value
        else:
            raise Exception("Royalties must be of type float")

    royalties = property(get_royalities, set_royalties)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in Contract.all if contract.date == date]


# The author property should be an instance of the Author class, while the book property should be an instance of the
# Book class. The date property should be a string that represents the date when the contract was signed,
# while the royalties property should be a number that represents the percentage of royalties that the author will
# receive for the book.
jackson = Author("Jackson")
cppfornewbs = Book("C++ for noobs")
contract1 = Contract(jackson, cppfornewbs, "asd", 3)
newcont = Contract(jackson, cppfornewbs, "asd", 4)

print(jackson.total_royalties())
