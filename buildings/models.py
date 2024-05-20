import hashlib
from datetime import datetime

from django.db import models
from django.utils.text import slugify

from bills.models import BillType
from user.models import User


class Building(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user"
    )
    bill_type = models.ManyToManyField(
        BillType, related_name="bill_type", blank=True
    )
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    home_mark = models.BooleanField(default=False)
    description = models.CharField(max_length=200, default="")
    currency = models.CharField(max_length=10, default="UAN")
    slug = models.SlugField(unique=True, blank=True)

    objects = models.Manager()

    def save(self, *args, **kwargs):
        if not self.slug:
            current_time = datetime.now().strftime('%Y%m%d%H%M%S')
            hash_object = hashlib.sha256(current_time.encode())
            hash_hex = hash_object.hexdigest()[:8]
            self.slug = slugify(f"{current_time}-{hash_hex}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.address
