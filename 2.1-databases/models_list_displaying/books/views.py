from django.shortcuts import render
from .models import Book


def books_view(req):
    template = 'books/books_list.html'

    context = {"books": Book.objects.all()}
    return render(req, template, context)
