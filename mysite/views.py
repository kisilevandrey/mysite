from django.http import HttpResponse
import datetime
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import HttpResponse
#from mysite.people.models import Person

def hello(request):
    return HttpResponse("Hello Django world")


def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html5 = t.render(Context({'current_date':now}))
    return HttpResponse(html5)


def index(request):
    html = "<h1>People</h1><hr>"
    return HttpResponse(html)