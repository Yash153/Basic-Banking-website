from django.contrib import admin
from .models import CustomerModel, TransferModel

# Register your models here.
admin.site.register(CustomerModel)
admin.site.register(TransferModel)