from django.shortcuts import render, redirect

books = [
    {
        "id": 1,
        "title": "Clean Code",
        "author": "Robert Martin",
        "price": 50
    }
]


def index(request):
    return render(request, "books/index.html", {"books": books})


def show(request, id):
    book = next((book for book in books if book["id"] == id), None)
    return render(request, "books/show.html", {"book": book})


def create(request):
    if request.method == "POST":
        books.append({
            "id": len(books) + 1,
            "title": request.POST["title"],
            "author": request.POST["author"],
            "price": int(request.POST["price"])
        })
        return redirect("/books")

    return render(request, "books/create.html")


def edit(request, id):
    book = next((book for book in books if book["id"] == id), None)

    if request.method == "POST":
        book["title"] = request.POST["title"]
        book["author"] = request.POST["author"]
        book["price"] = request.POST["price"]
        return redirect("/books")

    return render(request, "books/edit.html", {"book": book})


def delete(request, id):
    global books
    books = [book for book in books if book["id"] != id]
    return redirect("/books")