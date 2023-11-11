from django.contrib import admin

# Register your models here.
from order.models import Order, OrderProduct, ShopCart

class ShopCartAdmin(admin.ModelAdmin):
    list_display=['user','product','price','quantity','amount']
    list_filter=['user']



class OrderProductline(admin.TabularInline):
    model=OrderProduct
    readonly_fields=('user','product','price','quantity','amount')
    can_delete=False
    extra=0


class OrderProductAdmin(admin.ModelAdmin):
    list_display=['user','product','price','quantity','amount']
    list_filter=['user']

class OrderAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','phone','city','total','status']
    list_filter=['status']
    readonly_fields=('user','first_name','last_name','phone','city','total','ip','address','country','phone','city')
    inlines=[OrderProductline]



admin.site.register(ShopCart,ShopCartAdmin)    
admin.site.register(Order,OrderAdmin)    
admin.site.register(OrderProduct,OrderProductAdmin)    