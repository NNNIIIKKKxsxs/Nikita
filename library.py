class Library:
    def init(self):
        self.books = []

    def add_book(self, title):
        if not title or title.strip() == "":
            raise ValueError("Book title cannot be empty")

        if title in self.books:
            raise ValueError("Book already exists")

        self.books.append(title)
        return True

    def search_book(self, title):
        if not title or title.strip() == "":
            raise ValueError("Search title cannot be empty")

        for book in self.books:
            if book.lower() == title.lower():
                return True

        return False

    def borrow_book(self, title):
        if not title or title.strip() == "":
            raise ValueError("Book title cannot be empty")

        if title not in self.books:
            raise ValueError("Book not found")

        self.books.remove(title)
        return "Book borrowed"
