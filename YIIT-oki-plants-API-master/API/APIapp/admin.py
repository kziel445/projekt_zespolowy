from django.contrib import admin
from .models import Post, User, Category, Product, Order, OrderItem
from django.contrib.auth.admin import UserAdmin
from django.db import models
from tinymce.widgets import TinyMCE


class PostContent(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},

    }

admin.site.register(Post, PostContent)
admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)

