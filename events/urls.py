from django.conf.urls import url

from . import views as events
from pages import views as pages
from events.models import Event

events_list=Event.objects.values_list('permalink',flat=True)
events_list='|'.join(events_list)

# Это основное приложение проекта


urlpatterns = [
        url(r'^$', events.affiche, name='affiche'),
        # Проекты
        url(r'projects/$', events.projects, name='projects'),
        # Перехватываем только соответствующие тэгам проектов
        url(r'(?P<permalink>' + events_list + ')/', events.show_project, name='show_project'),
        # Команда
        url(r'team/$', events.guides, name='guides'),
        # Отдельный человек
        url(r'team/(?P<nick>\w+)/$', events.show_guide, name='show_guide'),
        # Фидбэк
        url(r'feedback/$', events.reviews, name='index'),
        # Ну и контакты
        url(r'contacts/$', pages.page, {"page": "contacts"}),
        ]
