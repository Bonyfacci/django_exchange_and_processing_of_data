from django.core.management.base import BaseCommand

from consumer.services import receive_from_kafka


class Command(BaseCommand):
    """
    ...
    """

    def handle(self, *args, **options):

        receive_from_kafka()
