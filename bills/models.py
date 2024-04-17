from datetime import datetime

from django.db import models

from user.models import User
from buildings.models import Building


class BillCategory(models.Model):
    category_name = models.CharField(max_length=50)
    color = models.CharField(max_length=30, default='Red')

    objects = models.Manager()

    def __str__(self):
        return self.category_name


class BillSubCategory(models.Model):
    sub_category_name = models.CharField(max_length=50)
    bill_category = models.ForeignKey(BillCategory, on_delete=models.CASCADE)
    tariff = models.DecimalField(max_digits=20, decimal_places=3, default=1)
    measure_unit = models.CharField(max_length=10, default='watt-hour')

    def __str__(self):
        return self.sub_category_name


class Bill(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    name = models.ForeignKey(BillSubCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=3)
    tariff = models.DecimalField(max_digits=20, decimal_places=3, default=1)
    month_paid = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField()
    bill_sum = models.DecimalField(max_digits=20, decimal_places=3, null=True, blank=True)

    objects = models.Manager()

    def save(self, *args, **kwargs):
        self.bill_sum = self.amount * self.tariff
        super().save(*args, **kwargs)
