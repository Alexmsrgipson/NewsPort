from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=64)
    text = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True)
    # TODO imgfield from ckeditor
    # TODO videofields from ckeditor


class Category(models.Model):
    name = models.CharField(max_length=64)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
