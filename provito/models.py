from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Board(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=64)
    content = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey('Board', on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    date_create = models.DateTimeField(auto_now_add=True)

    sent_for_approval = 'sent for approval'
    accepted = 'accepted'
    choice = (
        ('sent for approval', 'Отправлено на согласование'),
        ('accepted', 'Согласовано')
    )
    status = models.CharField(choices=choice, default=sent_for_approval, max_length=17)
    deleted = models.BooleanField(default=False)
