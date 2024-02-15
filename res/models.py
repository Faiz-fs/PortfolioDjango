from django.db import models

# Create your models here.

class Message(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField()
    msg=models.CharField(max_length=100)
