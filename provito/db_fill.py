from django.contrib.auth.models import User

from .models import *

"""
For fill db
py manage.py shell
from provito.db_fill import *
fill_category()
fill_boards()
"""

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
                         content='<pre><span style="font-size:14px"><strong>Продам дуло</strong></span></pre>'
                                 '<pre>Продам дуло, дырка нормальная<img alt="smiley" '
                                 'src="http://127.0.0.1:8000/static/ckeditor/ckeditor/plugins/smiley/images/regular_smile.png" '
                                 'style="height:23px; width:23px" title="smiley" /></pre>',
                         category=Category.objects.get(id=1))
    Board.objects.create(author=User.objects.get(id=1),
                         title='Куплю холм с кулями',
                         content='<pre><span style="font-size:14px"><strong>Куплю холм с кулями</strong></span></pre>'
                                 '<pre>Куплю холм, цена договорная<img alt="smiley" '
                                 'src="http://127.0.0.1:8000/static/ckeditor/ckeditor/plugins/smiley/images/regular_smile.png" '
                                 'style="height:23px; width:23px" title="smiley" /></pre>',
                         category=Category.objects.get(id=2))
    Board.objects.create(author=User.objects.get(id=1),
                         title='Продам что-то очень нужное',
                         content='<pre><span style="font-size:14px"><strong>Продам что-то очень нужное</strong></span></pre>'
                                 '<pre>Продам дупло, комфортабельное, цена в долларах<img alt="smiley" '
                                 'src="http://127.0.0.1:8000/static/ckeditor/ckeditor/plugins/smiley/images/regular_smile.png" '
                                 'style="height:23px; width:23px" title="smiley" /></pre>',
                         category=Category.objects.get(id=3))
    Board.objects.create(author=User.objects.get(id=1),
                         title='Продам дуло',
                         content='<pre><span style="font-size:14px"><strong>Продам дуло</strong></span></pre>'
                                 '<pre>Продам дуло, дырка нормальная<img alt="smiley" '
                                 'src="http://127.0.0.1:8000/static/ckeditor/ckeditor/plugins/smiley/images/regular_smile.png" '
                                 'style="height:23px; width:23px" title="smiley" /></pre>',
                         category=Category.objects.get(id=4))
    Board.objects.create(author=User.objects.get(id=1),
                         title='Куплю фантазию',
                         content='<pre><span style="font-size:14px"><strong>Куплю фантазию</strong></span></pre>'
                                 '<pre>Куплю фантазию. Своей уже не хватает<img alt="smiley" '
                                 'src="http://127.0.0.1:8000/static/ckeditor/ckeditor/plugins/smiley/images/regular_smile.png" '
                                 'style="height:23px; width:23px" title="smiley" /></pre>',
                         category=Category.objects.get(id=5))
    Board.objects.create(author=User.objects.get(id=1),
                         title='Выкую сапоги скороходы',
                         content='<pre><span style="font-size:14px"><strong>Выкую сапоги скороходы</strong></span></pre>'
                                 '<pre>Выкую сапоги скороходы, вес пол тонны каждый<img alt="smiley" '
                                 'src="http://127.0.0.1:8000/static/ckeditor/ckeditor/plugins/smiley/images/regular_smile.png" '
                                 'style="height:23px; width:23px" title="smiley" /></pre>',
                         category=Category.objects.get(id=6))
    Board.objects.create(author=User.objects.get(id=1),
                         title='Куплю Трусы кожаные',
                         content='<pre><span style="font-size:14px"><strong>Куплю Трусы кожаные</strong></span></pre>'
                                 '<pre>Куплю Трусы кожаные, бронированные<img alt="smiley" '
                                 'src="http://127.0.0.1:8000/static/ckeditor/ckeditor/plugins/smiley/images/regular_smile.png" '
                                 'style="height:23px; width:23px" title="smiley" /></pre>',
                         category=Category.objects.get(id=7))
    Board.objects.create(author=User.objects.get(id=1),
                         title='Наварю зельца',
                         content='<pre><span style="font-size:14px"><strong>Наварю зельца</strong></span></pre>'
                                 '<pre>Наварю зельца. Одна склянка два пинка<img alt="smiley" '
                                 'src="http://127.0.0.1:8000/static/ckeditor/ckeditor/plugins/smiley/images/regular_smile.png" '
                                 'style="height:23px; width:23px" title="smiley" /></pre>',
                         category=Category.objects.get(id=8))
    Board.objects.create(author=User.objects.get(id=1),
                         title='Сниму с глаз',
                         content='<pre><span style="font-size:14px"><strong>Сниму с глаз</strong></span></pre>'
                                 '<pre>Сниму с глаз, с ушей. Навешаю лапши<img alt="smiley" '
                                 'src="http://127.0.0.1:8000/static/ckeditor/ckeditor/plugins/smiley/images/regular_smile.png" '
                                 'style="height:23px; width:23px" title="smiley" /></pre>',
                         category=Category.objects.get(id=9))
    Board.objects.create(author=User.objects.get(id=1),
                         title='Видос с ютуба',
                         content='<p><iframe frameborder="0" height="400" scrolling="no" '
                                 'src="https://www.youtube.com/embed/fMZBTCRGMS8" width="500"></iframe></p>',
                         category=Category.objects.get(id=10))
