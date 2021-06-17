from django.contrib import admin
from .models import Product, Category, Brand, Subcategory, Type, Rating, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "subcategory",
        "type",
        "brand",
        "price",
        "stock",
        "date_added",
    )
    search_fields = (
        "title",
        "category__title",
        "subcategory__title",
        "type__title",
        "brand__name",
        "description",
    )
    readonly_fields = ("slug", "thumbnail","date_added")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "ordering")
    search_fields = ("title", "ordering")


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "parent", "ordering")
    search_fields = ("title", "parent__title", "ordering")


class TypeAdmin(admin.ModelAdmin):
    list_display = ("title", "parent", "ordering")
    search_fields = ("title", "parent__title", "ordering")


class RatingAdmin(admin.ModelAdmin):
    list_display = ("user_id", "product", "rating", "date_added")
    search_fields = (
        "user_id__email",
        "user_id__first_name",
        "user_id__last_name",
        "product__title",
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("rating", "headline", "date_added")
    search_fields = (
        "rating__user_id__email",
        "rating__user_id__first_name",
        "rating__user_id__last_name",
        "rating__product__title",
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Brand)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Product, ProductAdmin)
