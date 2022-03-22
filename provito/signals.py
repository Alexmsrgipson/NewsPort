from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.mail import send_mail

from .models import Comment, Board
from .tasks import send_email_new_comment


@receiver(post_save, sender=Comment)
def send_message(sender, instance, created, **kwargs):
    if created:
        id = instance.board_id
        board = Board.objects.get(id=id)
        email = board.author.email
        comment_author = User.objects.get(id=instance.author_id)

        # Celery and redis are unstable. Made direct sending

        # send_email_new_comment.apply_async(kwargs={
        #     'board_title': board.title,
        #     'comment_text': instance.text,
        #     'comment_author': comment_author,
        #     'email': email,
        # })

        send_mail(
            subject='Оповещение о новом комментарии',
            message=f'У вашего объявления "{board.title}" новый комментарий: {instance.text}.\n'
                    f'Автор комментария: {comment_author}',
            from_email='alex85aleshka@yandex.ru',
            recipient_list=[email],
        )
