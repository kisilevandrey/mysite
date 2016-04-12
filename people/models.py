from django.db import models

class Person(models.Model):
    name = models.CharField('name', max_length=200)
    email = models.EmailField('Email', blank = True)

