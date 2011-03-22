from django.core.management.base import BaseCommand
from django.db.models import get_models

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for model in get_models():
            print "%s : %d" % (str(model), model.objects.count())