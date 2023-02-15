from django.contrib import admin
from .models import Address, Category, Order, ShoppingUser,Subcategory,Product,ShoppingCart,CartItem

# Register your models here.
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product)
admin.site.register(Address)
admin.site.register(ShoppingUser)
admin.site.register(ShoppingCart)
admin.site.register(CartItem)
admin.site.register(Order)