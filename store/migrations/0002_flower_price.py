# Generated by Django 5.0.3 on 2024-03-10 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="flower",
            name="price",
            field=models.IntegerField(null=True),
        ),
    ]
