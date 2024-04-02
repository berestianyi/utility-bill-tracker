from django.db import models
from django.urls import reverse

from user.models import User


class Building(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    home_mark = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return self.address


class BillCategory(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, max_length=255, db_index=True)

    objects = models.Manager()

    def __str__(self):
        return self.name


class Bill(models.Model):
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=20, decimal_places=3)
    price = models.DecimalField(max_digits=20, decimal_places=3)
    created_at = models.DateTimeField(auto_now=True)
    bill_category = models.ForeignKey(BillCategory, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=255, db_index=True)

    objects = models.Manager()

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        # return reverse()
        pass