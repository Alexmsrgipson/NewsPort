from django import template
from datetime import datetime


register = template.Library()


@register.filter(name='time_elapsed')
def time_elapsed(value):
    # time = datetime.now() - datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f')
    print(value)
    print(type(value))
    print(datetime.now())
    time = datetime.now() - value
    time = time.total_seconds() / 60
    if time < 60:
        time = f'{int(time)} mins'
    elif 60 <= time <= 1439:
        time = f'{int(time/60)} hours'
    else:
        time = f'{int(time/60/24)} days'
    return time

# py manage.py shell
# from provito.templatetags.custom_filters import time_elapsed
# time_elapsed('2022-03-13 11:00:33.488929')