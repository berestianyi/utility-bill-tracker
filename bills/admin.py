from django.contrib import admin

from bills.models import Bill, BillSubCategory, BillCategory, Building

admin.site.register(Building)
admin.site.register(BillCategory)
admin.site.register(Bill)
admin.site.register(BillSubCategory)
