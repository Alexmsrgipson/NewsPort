from .models import *
from django.contrib.auth.models import User

# For fill db
# py manage.py shell
# from provito.db_fill import *
# fill_category()
# fill_boards()


def fill_category():
    Category.objects.create(name='Танки')
    Category.objects.create(name='Хилы')
    Category.objects.create(name='ДД')
    Category.objects.create(name='Торговцы')
    Category.objects.create(name='Гилдмастеры')
    Category.objects.create(name='Квестгиверы')
    Category.objects.create(name='Кузнецы')
    Category.objects.create(name='Кожевники')
    Category.objects.create(name='Зельевары')
    Category.objects.create(name='Мастера заклинаний')


def fill_boards():
    Board.objects.create(author=User.objects.get(id=1),
                         title='Продам дуло',
                         text='Продам дуло, дырка нормальная',
                         category=Category.objects.get(id=1))
    Board.objects.create(author=User.objects.get(id=1),
                         title='Куплю холм',
                         text='Куплю холм, цена договорная',
                         category=Category.objects.get(id=2))
    Board.objects.create(author=User.objects.get(id=1),
                         title='Продам что-то очень нужное',
                         text='Продам дупло, комфортабельное, цена в долларах',
                         category=Category.objects.get(id=3))
    Board.objects.create(author=User.objects.get(id=1),
                         title='Продам куплю',
                         text='Продам навык продавца',
                         category=Category.objects.get(id=4))
    Board.objects.create(author=User.objects.get(id=1),
                         title='Продам дуло',
                         text='Продам дуло, дырка нормальная',
                         category=Category.objects.get(id=5))
    Board.objects.create(author=User.objects.get(id=1),
                         title='Куплю фантазию',
                         text='КУплю фантазию. Своей уже не хватает',
                         category=Category.objects.get(id=6))
    Board.objects.create(author=User.objects.get(id=1),
                         title='Выкую сапоги скороходы',
                         text='Выкую сапоги скороходы, вес пол тонны каждый',
                         category=Category.objects.get(id=7))
    Board.objects.create(author=User.objects.get(id=1),
                         title='Куплю Трусы кожаные',
                         text='Куплю Трусы кожаные, бронированные',
                         category=Category.objects.get(id=8))
    Board.objects.create(author=User.objects.get(id=1),
                         title='Наварю зелььца',
                         text='Наварю зелььца. Одна клянка два пинка',
                         category=Category.objects.get(id=9))
    Board.objects.create(author=User.objects.get(id=1),
                         title='Сниму с глаз',
                         text='Сниму с глаз, с ушей. Навешаю лапши',
                         category=Category.objects.get(id=10))
