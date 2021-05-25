from django.contrib import admin
from .models import Product, Category, Brand, Subcategory

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'brand', 'price', 'date_added')
    search_fields = ('title', 'category', 'subcategories', 'brand', 'description')
    readonly_fields = ('date_added',)

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    search_fields = ('title', 'parent')


admin.site.register(Category)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)

