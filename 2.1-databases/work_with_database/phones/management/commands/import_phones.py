from django.utils.text import slugify
import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open("./phones.csv", newline="") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for i in reader:
                Phone.objects.create(
                    name=i["name"],
                    price=i["price"],
                    image=i["image"],
                    release_date=i["release_date"],
                    lte_exists=i["lte_exists"],
                    slug=slugify(i["name"])
                )
