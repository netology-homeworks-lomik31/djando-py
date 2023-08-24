from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
from os import listdir

def home_view(req):
    template_name = "app/home.html"
    pages = {
        "Главная страница": reverse("home"),
        "Показать текущее время": reverse("time"),
        "Показать содержимое рабочей директории": reverse("workdir")
    }
    context = {
        "pages": pages
    }
    return render(req, template_name, context)


def time_view(req):
    current_time =\
datetime.datetime.strftime(
    datetime.datetime.now(
        datetime.timezone(
            datetime.timedelta(hours=3)
        )
    ),
"%d.%m.%Y-%H:%M:%S")
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(req):
    res = "<br>".join(listdir("./"))
    return HttpResponse(res)
