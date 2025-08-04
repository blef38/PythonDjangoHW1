import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse

def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.datetime.now().time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории

    # Получаем список всех элементов в текущей рабочей директории
    files = os.listdir()

    # Фильтруем только файлы (исключаем директории)
    file_list = [f for f in files if os.path.isfile(f)]

    # Формируем HTML-ответ с списком файлов
    response_content = "<h1>Список файлов в рабочей директории:</h1><ul>"
    for file in file_list:
        response_content += f"<li>{file}</li>"
    response_content += "</ul>"

    return HttpResponse(response_content)

    #raise NotImplemented
