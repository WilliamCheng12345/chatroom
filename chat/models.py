from django.db import models
from django.urls import reverse

# Create your models here.
from django.utils.text import slugify


class Room(models.Model):
    room = models.CharField(
        max_length=100,
        primary_key=True
    )
    password = models.CharField(
        max_length=30
    )
    creator = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )

    slug = models.SlugField(
        unique=True
    )

    def __str__(self):
        return self.room

    def get_absolute_url(self):
        return reverse('chat', kwargs={'room_name': self.room})

class Message(models.Model):
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name='messages',
    )

    def __str__(self):
        return self.body