# Generated by Django 5.0.3 on 2024-04-05 11:36

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BillCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(default='Red', max_length=30)),
                ('is_selected', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='BillSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('is_selected', models.BooleanField(default=True)),
                ('bill_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bills.billcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('home_mark', models.BooleanField(default=False)),
                ('bill_sub_category', models.ManyToManyField(blank=True, related_name='buildings', to='bills.billsubcategory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buildings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=3, max_digits=20)),
                ('measure_unit', models.CharField(default='watt-hour', max_length=10)),
                ('price', models.DecimalField(decimal_places=3, max_digits=20)),
                ('month_paid', models.DateField(default=datetime.date.today)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bills.billsubcategory')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bills.building')),
            ],
        ),
    ]
