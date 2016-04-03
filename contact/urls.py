from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^$','contact.views.contact', name = 'contact'),
    ]