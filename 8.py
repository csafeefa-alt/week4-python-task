library = {}
def add_book(book_id, title, author):
    if book_id in library:
        print("Book ID already exists.")
    else:
        library[book_id] = {
            "title": title,
            "author": author,
            "issued": False
        }
        print("Book added successfully.")
def issue_book(book_id):
    if book_id not in library:
        print("Book not found.")
    elif library[book_id]["issued"]:
        print("Book already issued.")
    else:
        library[book_id]["issued"] = True
        print("Book issued successfully.")
def return_book(book_id):
    if book_id not in library:
        print("Book not found.")
    elif not library[book_id]["issued"]:
        print("Book was not issued.")
    else:
        library[book_id]["issued"] = False
        print("Book returned successfully.")
def search_book(keyword):
    found = False
    for book_id, details in library.items():
        if keyword.lower() in details["title"].lower() or \
           keyword.lower() in details["author"].lower():
            status = "Issued" if details["issued"] else "Available"
            print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Status: {status}")
            found = True
    if not found:
        print("No matching books found.")
while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        bid = int(input("Enter book ID: "))
        title = input("Enter title: ")
        author = input("Enter author: ")
        add_book(bid, title, author)
    elif choice == 2:
        bid = int(input("Enter book ID to issue: "))
        issue_book(bid)
    elif choice == 3:
        bid = int(input("Enter book ID to return: "))
        return_book(bid)
    elif choice == 4:
        key = input("Enter title or author to search: ")
        search_book(key)
    elif choice == 5:
        print("Exiting Library System.")
        break
    else:
        print("Invalid choice.")