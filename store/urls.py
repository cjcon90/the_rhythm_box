from django.urls import path
from .views import (
    index,
    shop,
)

urlpatterns = [
    path("", index, name="home"),
    path("shop/", shop, name="shop"),
    path("shop/<slug:category>/", shop, name="shop"),
    path("shop/<slug:category>/<slug:subcategory>/", shop, name="shop"),
    path(
        "shop/<slug:category>/<slug:subcategory>/<slug:type>/",
        shop,
        name="shop",
    ),
]
