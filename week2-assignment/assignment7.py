
library = {
    "books": [],
    "borrowed_books": [],
}

def add_book(title, author):
    library["books"].append({"title": title, "author": author, "borrowed": False})

def borrow_book(title, borrower):
    for book in library["books"]:
        if book["title"] == title and not book["borrowed"]:
            book["borrowed"] = True
            library["borrowed_books"].append({"title": title, "borrower": borrower})
            return f"{title} has been borrowed by {borrower}."
    return f"{title} is not available for borrowing."

# Test
add_book("Harry Potter", "Himal Tamang")
add_book("The Hobbit", "Sangam Mishra")

print(borrow_book("Harry Potter", "John Doe"))
print(borrow_book("The Hobbit", "Jane Doe"))
print("Library:", library)

