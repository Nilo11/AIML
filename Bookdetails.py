class Bookdetails:
    def __init__(self, title, author, total_copies):
        self.title = title
        self.author = author
        self.available_copies = total_copies

    def issue_book(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print(f"Book '{self.title}' issued successfully.")
        else:
            print(f"Sorry, '{self.title}' is currently out of stock.")

    def return_book(self):
        self.available_copies += 1
        print(f"Book '{self.title}' returned successfully.")

    def display_details(self):
        print(f"Title: {self.title} | Author: {self.author} | Copies Available: {self.available_copies}")

# Example Usage:
book1 = Bookdetails("Python Programming", "Guido van Rossum", 2)
book1.display_details()
book1.issue_book()
book1.issue_book()
book1.issue_book()  # Should state out of stock
book1.return_book()
book1.display_details()
