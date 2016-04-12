from django.shortcuts import render
from django.shortcuts import HttpResponse
#from mysite.people.models import Person

def index(request):
    html = "<h1>People</h1><hr>"
    return HttpResponse(html)