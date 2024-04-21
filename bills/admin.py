from django.contrib import admin

from bills.models import Bill, BillType

admin.site.register(BillType)
admin.site.register(Bill)
