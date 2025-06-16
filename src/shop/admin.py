from django.contrib import admin
from .models import Product, Order, OrderItem
from django.contrib.sessions.models import Session

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['session_key', 'get_decoded', 'expire_date']

    def get_decoded(self, obj):
        return obj.get_decoded()
    get_decoded.short_description = 'Data'
    
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
