from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    stars = models.IntegerField(default=1)
    comment = models.TextField(null=True, blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-posted_at',)

    def __str__(self):
        return self.name