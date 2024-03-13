import random

from django.core.management.base import BaseCommand

from store.models import Flower, Fertilizers

FLOWER_DATA = [
    {"name": "Hydrangea", "color": "Blue", "image": "static/store/Hydrangea.png"},
    {"name": "Rose", "color": "Red", "image": "static/store/Rose.png"},
    {"name": "Gypsophila", "color": "White", "image": "static/store/Gypsophila.png"},
]

FERTILIZERS_DATA = [{"name": "Green Boots"}, {"name": "Burpee"}, {"name": "Happy flower"}]


class Command(BaseCommand):
    help = "Add the number of generations or just run the command, the default number of generations is 50 "

    def add_arguments(self, parser):
        parser.add_argument("number", type=int, nargs="?", default=50)

    def handle(self, *args, **options):
        number = options["number"]

        Flower.objects.all().delete()
        Fertilizers.objects.all().delete()

        fertilizers = [
            Fertilizers.objects.create(code=random.randint(10000, 999999), name=data["name"])
            for data in FERTILIZERS_DATA
        ]
        rand_code = random.randint(10000, 9999999)

        for _ in range(number):
            for data in FLOWER_DATA:
                price = random.randint(50, 500)
                flower = Flower(
                    name=data["name"],
                    passport_number=rand_code,
                    color=data["color"],
                    fertilizer=random.choice(fertilizers),
                    price=price,
                )

                with open(data["image"], 'rb') as img_file:
                    flower.image.save(data["image"], img_file, save=True)
                flower.save()

        self.stdout.write(self.style.SUCCESS("The data was successfully generated"))
