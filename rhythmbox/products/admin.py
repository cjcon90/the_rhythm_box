from django.contrib import admin
from .models import Product, Category, Brand, Subcategory, Feature

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'brand', 'price', 'date_added')
    search_fields = ('title', 'category', 'subcategories', 'features', 'brand', 'description')
    readonly_fields = ('date_added',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'ordering')
    search_fields = ('title', 'ordering')

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'ordering')
    search_fields = ('title', 'parent', 'ordering')

class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'ordering')
    search_fields = ('title', 'parent', 'ordering')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)

