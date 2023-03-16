from django.contrib import admin

# Register your models here.
from ecart.models import Category
from ecart.models import Products
from ecart.models import Cart
from ecart.models import Reviews


# Register your models here.
admin.site.register(Category)

admin.site.register(Products)

admin.site.register(Cart)

admin.site.register(Reviews)
