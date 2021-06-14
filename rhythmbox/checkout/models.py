import uuid
from decimal import Decimal

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from accounts.models import Account
from products.models import Product


class Order(models.Model):
    order_number = models.CharField(max_length=32, editable=False)
    user = models.ForeignKey(
        Account,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    country = CountryField(blank=False, default="IE")
    postcode = models.CharField(max_length=20)
    town_or_city = models.CharField(max_length=40)
    street_address_1 = models.CharField(max_length=80)
    street_address_2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=8, decimal_places=2, default=0
    )
    order_total = models.DecimalField(
        max_digits=12, decimal_places=2, default=0
    )
    grand_total = models.DecimalField(
        max_digits=12, decimal_places=2, default=0
    )

    def update_total(self):
        """
        Update total every time a line item is added,
        accounting for delivery costs
        """
        self.order_total = (
            self.lineitems.aggregate(Sum("lineitem_total"))[
                "lineitem_total__sum"
            ]
            or 0
        )
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * Decimal(
                settings.STANDARD_DELIVERY_PERCENTAGE / 100
            )
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the
        order number if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="lineitems",
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, editable=False
    )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"ProductID {self.product.id} on order {self.order.order_number}"
        )