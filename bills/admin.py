from django.contrib import admin

from bills.models import Bill, BillSubCategory, BillCategory

admin.site.register(BillCategory)
admin.site.register(Bill)
admin.site.register(BillSubCategory)
