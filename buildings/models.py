from django.db import models
from user.models import User
from bills.models import BillSubCategory


class Building(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buildings')
    bill_sub_category = models.ManyToManyField(BillSubCategory, related_name='bill_sub_category', blank=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    home_mark = models.BooleanField(default=False)
    description = models.CharField(max_length=200, default='')
    currency = models.CharField(max_length=10, default='UAN')

    objects = models.Manager()

    def __str__(self):
        return self.address
