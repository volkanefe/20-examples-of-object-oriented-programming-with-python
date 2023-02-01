# Class definition with special methods
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages"
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print(f"{self.title} has been deleted.")

# Object creation and usage with special methods
book = Book("Pride and Prejudice", "Jane Austen", 288)
print(book) # Output: Pride and Prejudice by Jane Austen, 288 pages
print(len(book)) # Output: 288
del book
# Output: Pride and Prejudice has been deleted.
