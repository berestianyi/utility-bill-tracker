# Generated by Django 5.0.3 on 2024-04-14 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0008_alter_bill_created_at_alter_bill_tariff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billsubcategory',
            old_name='sub_category_name',
            new_name='name',
        ),
    ]
