from django.shortcuts import render, redirect
from .models import Phone


def index(req):
    return redirect("catalog")


def show_catalog(req):
    template = "catalog.html"
    sort = req.GET.get("sort", "id")
    if sort == "name": pass
    elif sort == "max_price": sort = "-price"
    elif sort == "min_price": sort = "price"
    else: sort = "id"
    context = {"phones": Phone.objects.all().order_by(sort)}
    return render(req, template, context)


def show_product(req, slug):
    template = "product.html"
    phone = Phone.objects.filter(slug=slug)
    context = {"phone": phone[0]}
    return render(req, template, context)
