from django.db import models

# Create your models here.

class UserPos(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class User(models.Model):
    login = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    position = models.ForeignKey('UserPos', on_delete=models.PROTECT)
    def __str__(self):
        return self.login