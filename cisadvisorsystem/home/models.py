from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.

class Response(models.Model):
    category = models.CharField(max_length=100, null=True, blank=True)
    question = models.TextField()
    response1 = models.TextField()
    response2 = models.TextField()

    def __str__(self):
        return self.question

class Message(models.Model):
    name = models.CharField(max_length=100)  # Name of the sender
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}: {self.text[:30]}"