from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Book
from .forms import BookForm

def index(request):
    books = Book.objects.all()
    return render(request, "books/index.html", {"books": books})


def show(request, id):
    book = get_object_or_404(Book, id=id)
    book.views += 1
    book.save()
    return render(request, "books/show.html", {"book": book})


@login_required # Requirement 2: Requires login to create
def create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user # Requirement 1: Assign to logged-in user
            book.save()
            form.save_m2m()
            return redirect("/books/")
    else:
        form = BookForm()
    return render(request, "books/create.html", {"form": form})


@login_required
def edit(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("/books/")
    else:
        form = BookForm(instance=book)
    return render(request, "books/edit.html", {"form": form, "book": book})


@login_required
@permission_required('books.delete_book', raise_exception=True) # Requirement 3: Requires permission privilege
def delete(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect("/books/")


# Auth Signup view
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Automatically logs user in after signing up
            return redirect("/books/")
    else:
        form = UserCreationForm()
    return render(request, "auth/signup.html", {"form": form})