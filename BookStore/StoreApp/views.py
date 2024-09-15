from django.shortcuts import render, redirect

from .forms import BookForm
from .models import *


def login(request):
    return render(request, 'login.html')


def index(request):
    if not request.user.is_authenticated or request.user.role != 'author':
        return render(request, 'index.html')
    booksAuthors = BookAuthor.objects.filter(author__user=request.user)
    books = Book.objects.filter(id__in=booksAuthors.values_list('book_id', flat=True))
    return render(request, 'index.html', context={'books': books})


def add_book(request):
    if request.method == "POST":
        form_data = BookForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            book = form_data.save(commit=False)
            book.save()
            bookAuthor = BookAuthor(book=book, author=Author.objects.get(user=request.user))
            bookAuthor.save()
            return redirect('/index')
    return render(request, 'add_book.html', {'form': BookForm})


def edit_book(request, pk):
    book_instance = Book.objects.filter(id=pk).get()
    if request.method == "POST":
        form_data = BookForm(data=request.POST, files=request.FILES, instance=book_instance)
        if form_data.is_valid():
            form_data.save()
        return redirect('/index')
    else:
        book = BookForm(instance=book_instance)
    return render(request, 'edit_book.html', context={'form': book})


def delete_book(request, pk):
    book_instance = Book.objects.filter(id=pk).get()
    if request.method == "POST":
        book_instance.delete()
        return redirect('/index')
    return render(request, 'delete_book.html')
