from django.db import models

# Create your models here.
class Room(models.Model):
    room = models.CharField(
        max_length=100,
        primary_key=True,
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.room

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