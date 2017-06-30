from website.slogans import slogans
import random
from django.urls import reverse

def slogans_gen(request):
    slogan = random.choice(slogans)
    return {'slogan': slogan}

def main_menu(request):
    main_menu = [
    {
    "url":"/",
    "title":"Афиша",
    },
    {
    "url": reverse('projects_index'),
    "title": "Наши проекты",
    },
    {
    "url":reverse('team'),
    "title":"Команда",
    },
    {
    "url":"/contacts/",
    "title":"Дружба и контакты",
    },
    {
    "url":"/feedback/",
    "title":"Отзывы",
    },
    ]
    return {'main_menu':main_menu}
