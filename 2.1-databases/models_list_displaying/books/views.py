from django.shortcuts import render
from .models import Book


def books_view(req):
    template = 'books/books_list.html'

    context = {"books": Book.objects.all()}
    return render(req, template, context)

def books_date_view(req, date):
    template = 'books/books_list_by_date.html'

    books = Book.objects.filter(pub_date = date)
    next_date = Book.objects.filter(pub_date__gt = date).order_by("pub_date").first()
    previous_date = Book.objects.filter(pub_date__lt = date).order_by("-pub_date").first()
    
    context = {
        "books": books,
        "previous_date": previous_date.pub_date.strftime("%Y-%m-%d") if previous_date else None,
        "next_date": next_date.pub_date.strftime("%Y-%m-%d") if next_date else None
    }
    return render(req, template, context)
