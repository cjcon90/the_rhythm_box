from django.contrib import admin
from .models import Product, Category, Brand, Subcategory, Type, Review

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'subcategory', 'type', 'brand', 'price', 'stock', 'date_added')
    search_fields = ('title', 'category__title','subcategory__title', 'type__title', 'brand__name', 'description')
    readonly_fields = ('date_added',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'ordering')
    search_fields = ('title', 'ordering')

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'ordering')
    search_fields = ('title', 'parent__title', 'ordering')

class TypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'ordering')
    search_fields = ('title', 'parent__title', 'ordering')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('headline', 'author', 'product', 'rating', 'date_added')
    search_fields = ('author__email', 'author__first_name', 'author__last_name', 'product__title')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Brand)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Product, ProductAdmin)

