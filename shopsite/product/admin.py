from django.contrib import admin
from .models import Category,product

@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    list_display = ["name","slug"]
    prepopulated_fields = {'slug':('name',)}

@admin.register(product)
class productadmin(admin.ModelAdmin):
    list_display = ["name","price","available","created","updated","category"]
    prepopulated_fields = {'slug':('name',)}