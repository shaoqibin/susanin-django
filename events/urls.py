from django.conf.urls import url

from . import views
from pages import views as pages
from events.models import Event

events_list=Event.objects.values_list('permalink',flat=True)
events_list='|'.join(events_list)

urlpatterns = [
        url(r'^$', views.afisha, name='index'),
        url(r'projects/$', views.index, name='index'),
        url(r'(?P<permalink>' + events_list + ')/', views.show_event, name='show_event'),
#        url(r'projects/(?P<permalink>\w+)/', views.show_event, name='show_event'),
        url(r'team/$', views.team, name='index'),
        url(r'team/(?P<nick>\w+)/$', views.show_guide, name='show_guide'),
        url(r'feedback/$', views.reviews, name='index'),
        url(r'contacts/$', pages.page, {"page": "contacts"}),
        ]
