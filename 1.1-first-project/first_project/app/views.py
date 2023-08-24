from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
from os import listdir


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': '',
        'Показать содержимое рабочей директории': ''
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(req):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
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
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    res = "<br>".join(listdir("./"))
    return HttpResponse(res)
