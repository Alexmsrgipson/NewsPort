from django.contrib import admin

from .models import Category, Board, Comment

class BoardAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = [field.name for field in Board._meta.get_fields()]
    # генерируем список имён всех полей для более красивого отображения
    list_filter = ('title', 'category')  # добавляем примитивные фильтры в нашу админку
    # search_fields = ('category')  # тут всё очень похоже на фильтры из запросов в базу


admin.site.register(Category)
# admin.site.register(Board, BoardAdmin)
admin.site.register(Board)
# admin.site.unregister(Board)
admin.site.register(Comment)

