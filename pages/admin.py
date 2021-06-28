from django.contrib import admin
from .models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category_id')

admin.site.register(product, ProductAdmin)
admin.site.register(User)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category , CategoryAdmin)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Order_items)