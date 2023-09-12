from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect("catalog")


def show_catalog(request):
    template = "catalog.html"
    context = {"phones": Phone.objects.all()}
    return render(request, template, context)


def show_product(request, slug):
    template = "product.html"
    phone = Phone.objects.filter(slug=slug)
    context = {"phone": phone[0]}
    return render(request, template, context)
