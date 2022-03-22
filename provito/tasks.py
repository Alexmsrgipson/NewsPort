from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User


@shared_task
def send_email(**kwargs):
    """
    Sending a message when the comment is accepted
    :param kwargs:
    :return:
    """
    send_mail(
        subject='Ваш комментарий акцептован',
        message=f'Автор объявления {kwargs["board_author"]} акцептовал ваш комментарий "{kwargs["comment_text"]}"',
        from_email='alex85aleshka@yandex.ru',
        recipient_list=[kwargs['user_email']],
    )


@shared_task
def send_email_new_comment(**kwargs):
    """
    Send a message to the author about a new comment
    :param kwargs:
    :return:
    """
    send_mail(
        subject='Оповещение о новом комментарии',
        message=f'У вашего объявления "{kwargs["board_title"]}" новый комментарий: {kwargs["comment_text"]}.\n'
                f'Автор комментария: {kwargs["comment_author"]}',
        from_email='alex85aleshka@yandex.ru',
        recipient_list=[kwargs["email"]],
    )
