from __future__ import unicode_literals

from django.db import models

class login(models.Model):
    users = models.CharField(max_length=25)
    password = models.CharField(max_length=10)

    def __str__(self):              # __unicode__ on Python 2
        return self.users

class tarea(models.Model):
    description = models.TextField(max_length=200)
    priority = models.CharField(max_length=200)
    users = models.CharField(max_length=25)

    def __str__(self):              # __unicode__ on Python 2
        return self.description