"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mysite.views import hello
from mysite.views import current_datetime
from django.http import HttpResponse

a = 0
def hey(request): # счетчик количества запросов
    global a
    a = a+1
    return HttpResponse(a)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^hello/$', hello),
    url('^time/$', current_datetime),
    url(r'^counter/$', hey)
]
