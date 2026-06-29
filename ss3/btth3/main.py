from fastapi import FastAPI
app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Python Basic",
        "author": "Lê Minh Thu",
        "category": "programming",
        "year": 2022,
        "is_available": True,
        "total_books": 6,
        "available_books": 4,
        "borrowed_books": 2
    },
    {
        "id": 2,
        "title": "Web API Design",
        "author": "Phạm Lan Hồng",
        "category": "web",
        "year": 2021,
        "is_available": False,
        "total_books": 4,
        "available_books": 2,
        "borrowed_books": 6
    },
    {
        "id": 3,
        "title": "Database System",
        "author": "Lê Minh Huyền",
        "category": "database",
        "year": 2020,
        "is_available": True,
        "total_books": 6,
        "available_books": 2,
        "borrowed_books": 4
    },
    {
        "id": 4,
        "title": "Clean Code",
        "author": "Lê Ánh Linh",
        "category": "programming",
        "year": 2008,
        "is_available": False,
        "total_books": 7,
        "available_books": 5,
        "borrowed_books": 3
    },
    {
        "id": 5,
        "title": "Computer Network",
        "author": "Vũ Hồng Vân",
        "category": "network",
        "year": 2019,
        "is_available": True,
        "total_books": 5,
        "available_books": 3,
        "borrowed_books": 7
    }
]

@app.get("/books/available")
def get_books_avai():
    avai_books = []

    for book in books:
        if book["is_available"] == True:
            avai_books.append(book)

    return avai_books

@app.get("/books/borrowed")
def get_books_borrowed():
    borrowed_books = []

    for book in books:
        if book["is_available"] == False:
            borrowed_books.append(book)

    return borrowed_books