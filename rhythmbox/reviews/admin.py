from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('headline', 'author', 'product', 'rating', 'date_added')
    search_fields = ('author__email', 'author__first_name', 'author__last_name', 'product__title')


admin.site.register(Review, ReviewAdmin)
