class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


# Creating a Book object
book = Book("1984", "Fairy Tale", 600)

# Displaying book information
book.display()
