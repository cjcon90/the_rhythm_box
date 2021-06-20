from products.models import Product, Category

def brands_per_category(request):
    """
    function to list brands associated with each
    product category, for shop page and footer sitemap
    """
    context = {}
    context["categories"] = Category.objects.all()
    context["category_brands"] = {}
    for category in context["categories"]:
        context["category_brands"][category] = sorted(set(
            Product.objects.filter(category=category).values_list(
                "brand__name", flat=True
            )
        ))
    return context