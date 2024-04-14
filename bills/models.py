from django.db import models

from user.models import User


class BillCategory(models.Model):
    category_name = models.CharField(max_length=50)
    color = models.CharField(max_length=30, default='Red')
    is_selected = models.BooleanField(default=True)

    objects = models.Manager()

    def __str__(self):
        return self.category_name


class BillSubCategory(models.Model):
    sub_category_name = models.CharField(max_length=50)
    is_selected = models.BooleanField(default=True)
    bill_category = models.ForeignKey(BillCategory, on_delete=models.CASCADE)
    tariff = models.DecimalField(max_digits=20, decimal_places=3, default=1)
    measure_unit = models.CharField(max_length=10, default='watt-hour')

    def __str__(self):
        return self.sub_category_name


class Building(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buildings')
    bill_sub_category = models.ManyToManyField(BillSubCategory, related_name='buildings', blank=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    home_mark = models.BooleanField(default=False)
    description = models.CharField(max_length=200, default='')

    objects = models.Manager()

    def __str__(self):
        return self.address


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
