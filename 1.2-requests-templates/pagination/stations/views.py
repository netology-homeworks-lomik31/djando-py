from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(req):
    return redirect(reverse("bus_stations"))

with open("./data-398-2018-08-30.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for i in reader:
            data.append(i)

def bus_stations(req):
    if "page" not in req.GET: return redirect(reverse("bus_stations") + "?page=1")
    try: int(req.GET["page"])
    except: return redirect(reverse("bus_stations") + "?page=1")

    p = Paginator(data, 10)
    page = p.get_page(req.GET["page"])
    context = {
        "page": page,
    }
    return render(req, "stations/index.html", context)
