from django.contrib import admin

from .models import Category, Board, Comment


admin.site.register(Category)
admin.site.register(Board)
admin.site.register(Comment)
