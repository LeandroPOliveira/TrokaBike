from django.contrib import admin
from .models import Address, Order, OrderItem


# Register the model on the admin section thing
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(OrderItem)
