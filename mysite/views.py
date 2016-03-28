from django.http import HttpResponse
import datetime
from django.template.loader import get_template
from django.template import Context


def hello(request):
    return HttpResponse("Hello Django world")


def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html5 = t.render(Context({'current_date':now}))
    return HttpResponse(html5)
