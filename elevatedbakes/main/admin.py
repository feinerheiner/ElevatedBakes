from django.contrib import admin
from .models import Gallery, Message, Invoice, Order


# Register your models here.
admin.site.register(Gallery)
admin.site.register(Message)
admin.site.register(Invoice)
admin.site.register(Order)


