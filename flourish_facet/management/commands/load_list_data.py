from edc_list_data import PreloadData
from django.core.management.base import BaseCommand
from ...list_data import list_data


class Command(BaseCommand):
    help = 'Load list data'

    def handle(self, *args, **kwargs):
        PreloadData(list_data=list_data)
        self.stdout.write(self.style.SUCCESS(
            f'List data successfully loaded.'))
