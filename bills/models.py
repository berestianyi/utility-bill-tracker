from datetime import time
from decimal import Decimal

from colorfield.fields import ColorField
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from user.models import User


class BillType(models.Model):
    COLOR_PALETTE = [
        (
            "#2D2A60",
            "blue",
        ),
        (
            "#154D47",
            "light-blue",
        ),
        (
            "#5B1070",
            "purple",
        ),
        (
            "#343434",
            "dark-grey",
        ),
        (
            "#777777",
            "light-grey",
        ),
        (
            "#183D22",
            "light-green",
        ),
        (
            "#072302",
            "dark-green",
        ),
        (
            "#421717",
            "red",
        ),
        (
            "#56135B",
            "pink",
        ),
        (
            "#705605",
            "yellow",
        ),
        (
            "#623307",
            "orange",
        ),
        ("#1B1D1E", "dark"),
    ]

    BOOSTRAP_COLOR_DICT = {
        "#2D2A60": "primary",
        "#154D47": "info",
        "#5B1070": "primary",
        "#343434": "light",
        "#777777": "secondary",
        "#183D22": "success",
        "#072302": "success",
        "#421717": "danger",
        "#56135B": "danger",
        "#705605": "warning",
        "#623307": "warning",
        "#1B1D1E": "light",
    }

    type_name = models.CharField(max_length=50)
    tariff = models.DecimalField(max_digits=20, decimal_places=3, default=1)
    measure_unit = models.CharField(max_length=10, default="watt-hour")
    slug = models.SlugField(unique=True, blank=True)
    is_deletable = models.BooleanField(default=False)
    color = ColorField(choices=COLOR_PALETTE, default="#1b1d1e")
    bootstrap_color = models.CharField(default="light")

    objects = models.Manager()

    def save(self, *args, **kwargs):
        if not self.slug:
            strtime = "".join(str(time()).split("."))
            string = "%s-%s" % (strtime[7:], self.type_name)
            self.slug = slugify(string)
        self.bootstrap_color = self.__class__.BOOSTRAP_COLOR_DICT.get(
            self.color
        )
        super(BillType, self).save()

    def __str__(self):
        return self.type_name


from buildings.models import Building


class Bill(models.Model):

    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    name = models.ForeignKey(BillType, on_delete=models.CASCADE)
    amount = models.DecimalField(
        max_digits=20, decimal_places=3, null=True, blank=True
    )
    tariff = models.DecimalField(
        max_digits=20, decimal_places=3, null=True, blank=True
    )
    month_paid = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    bill_sum = models.DecimalField(
        max_digits=20, decimal_places=2, null=True, blank=True
    )
    bill_file = models.FileField(
        upload_to="uploads_model", null=True, blank=True
    )

    objects = models.Manager()

    def save(self, *args, **kwargs):
        strtime = "".join(str(time()).split("."))
        string = "%s-%s" % (strtime[7:], self.name)
        self.slug = slugify(string)
        if not self.tariff:
            self.tariff = self.name.tariff
        if not self.bill_sum:
            self.bill_sum = Decimal(self.amount) * Decimal(self.name.tariff)
        super(Bill, self).save()

    def str_time(self):
        date_created = self.created_at.strftime("%d.%m.%Y")
        return date_created

    @staticmethod
    def total_sum(building_slug):
        building_bills = Bill.objects.all().filter(
            building__slug=building_slug
        )
        total = sum(bill.bill_sum for bill in building_bills)
        return total
