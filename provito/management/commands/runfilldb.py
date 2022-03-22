from django.core.management.base import BaseCommand
from provito.db_fill import fill_category, fill_boards


class Command(BaseCommand):
    help = 'Заполняем базу данных'

    def handle(self, *args, **options):
        try:
            fill_category()
            fill_boards()
            self.stdout.write(self.style.SUCCESS(
                f'Succesfully load data in db'))
        except BaseException as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
