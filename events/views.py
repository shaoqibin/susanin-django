from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Event, Guide, Review

# Create your views here.

def afisha(request):
    return render(request, 'events/afisha.html', {})

def team(request):
    team = Guide.objects.all()
    return render(request, 'events/team.html', {"team": team})

def show_guide(request, nick):
    guide = Guide.objects.get(nick=nick)
    return render(request, 'events/show_guide.html', {"guide": guide})

def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'events/reviews.html', {"reviews": reviews})

def index(request):
    events = Event.objects.all()
    template = loader.get_template('events/index.html')
    context = {
            'events': events,
            }
    return HttpResponse(template.render(context, request))

def show_event(request, permalink):
    event = Event.objects.get(permalink=permalink)
    return render(request, 'events/show_event.html', {"event":event})
