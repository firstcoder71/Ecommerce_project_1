from django.contrib import admin

from .models import (
    Customer,
    Products,
    Cart,
    Contact,
    OrderPlaced
)

# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display =['id', 'user', 'name', 'surname','email','country','area','state','region','address_line_1','address_line_2','postcode','mobile_number','image']

@admin.register(Products)
class ProductModelAdmin(admin.ModelAdmin):
    list_display =['id', 'title','product_name','selling_price','discounted_price','description','brand','category','product_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','product','quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer','product','quantity','ordered_date','status']
@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email','message']
