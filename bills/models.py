from datetime import date

from django.db import models

from user.models import User


class Building(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    home_mark = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return self.address


class BillCategory(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=30, default='Red')
    is_selected = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, max_length=255, db_index=True)

    objects = models.Manager()

    def __str__(self):
        return self.name


class BillSubCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=255, db_index=True)
    is_selected = models.BooleanField(default=True)
    bill_category = models.ForeignKey(BillCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Bill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.ForeignKey(BillSubCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=3)
    measure_unit = models.CharField(max_length=10, default='watt-hour')
    price = models.DecimalField(max_digits=20, decimal_places=3)
    month_paid = models.DateField(default=date.today)
    created_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse()
        pass
