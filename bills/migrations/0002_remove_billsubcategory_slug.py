# Generated by Django 5.0.3 on 2024-04-06 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billsubcategory',
            name='slug',
        ),
    ]