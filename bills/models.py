from datetime import datetime
from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from user.models import User


class BillType(models.Model):
    type_name = models.CharField(max_length=50)
    tariff = models.DecimalField(max_digits=20, decimal_places=3, default=1)
    measure_unit = models.CharField(max_length=10, default='watt-hour')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.type_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.type_name


from buildings.models import Building


class Bill(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    name = models.ForeignKey(BillType, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=3)
    tariff = models.DecimalField(max_digits=20, decimal_places=3, default=1)
    month_paid = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    bill_sum = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)

    objects = models.Manager()

    def save(self, *args, **kwargs):
        self.tariff = self.name.tariff
        self.bill_sum = self.amount * self.tariff
        super().save(*args, **kwargs)

    def str_time(self):
        date_created = self.created_at.strftime('%d.%m.%Y')
        return date_created

    @staticmethod
    def total_sum(building_slug):
        building_bills = Bill.objects.all().filter(building__slug=building_slug)
        total = sum(bill.bill_sum for bill in building_bills)
        return total
