from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CustomerProfile)
admin.site.register(Categories)
admin.site.register(Events)
admin.site.register(VendorProfile)
admin.site.register(Order)