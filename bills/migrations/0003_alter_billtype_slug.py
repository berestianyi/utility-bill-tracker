# Generated by Django 5.0.3 on 2024-04-21 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bills", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="billtype",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
