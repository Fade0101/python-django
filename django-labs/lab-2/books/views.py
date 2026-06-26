# books/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

def index(request):
    books = Book.objects.all()
    return render(request, "books/index.html", {"books": books})


def show(request, id):
    book = get_object_or_404(Book, id=id)
    # Increment view count whenever details page is fetched
    book.views += 1
    book.save()
    return render(request, "books/show.html", {"book": book})


# books/views.py

def create(request):
    if request.method == "POST":
        Book.objects.create(
            title=request.POST["title"],
            desc=request.POST["desc"],
            rate=int(request.POST.get("rate", 0)),
            views=0
        )
        return redirect("/books/")

    return render(request, "books/create.html")


def edit(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        book.title = request.POST["title"]
        book.desc = request.POST["desc"]
        book.rate = int(request.POST.get("rate", 0))
        book.save()
        return redirect("/books/")

    return render(request, "books/edit.html", {"book": book})


def delete(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect("/books/")