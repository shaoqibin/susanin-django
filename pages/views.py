from django.shortcuts import render
from django.http import HttpResponse

from .models import Page
import logging
# Create your views here.

def page(request, page):
    #logging.debug(page)
    #return HttpResponse(page)
    obj = Page.objects.get(permalink=page)
    return render(request, 'pages/page.html', {"obj": obj});
