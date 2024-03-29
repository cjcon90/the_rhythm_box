from io import BytesIO
from PIL import Image
import random
import string

from django.core.files import File
from django.db import models
from django.db.models import Avg
from django.template.defaultfilters import slugify
from django.core.validators import MinValueValidator, MaxValueValidator

from accounts.models import Account


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ("ordering", "title")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Overwrite default save and create product slug
        """
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Subcategory(models.Model):
    parent = models.ForeignKey(
        Category, related_name="subcategories", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Subcategories"
        ordering = ("parent", "ordering", "title")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Type(models.Model):
    parent = models.ForeignKey(
        Subcategory, related_name="types", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Types"
        ordering = ("parent", "ordering", "title")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Brand(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    logo = models.ImageField(upload_to="brands/", blank=False, null=False)

    class Meta:
        verbose_name_plural = "Brands"
        ordering = ("name",)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    subcategory = models.ForeignKey(
        Subcategory, related_name="subcategory", on_delete=models.CASCADE
    )
    type = models.ForeignKey(
        Type,
        related_name="type",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    brand = models.ForeignKey("Brand", null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.IntegerField(default=15)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    thumbnail = models.ImageField(
        upload_to="products/thumbnails/", blank=True, null=True
    )
    product_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ("-date_added",)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Modified save method to update thumbnail only if object is
        new, or the object image has been updated
        """
        if self.pk is None:
            self.thumbnail = self.make_thumbnail(self.image)
        else:
            original = Product.objects.get(id=self.pk)
            if original.image != self.image:
                self.thumbnail = self.make_thumbnail(self.image)
        self.slug = slugify(self.title)
        self.product_code = self.get_product_code()
        super().save(*args, **kwargs)

    def make_thumbnail(self, image, size=(300, 200)):
        """
        Method which automatically makes thumbnail images
        of the main uploaded image, reducing size to 300x200
        """
        img = Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, "JPEG", quality=85)
        thumbnail = File(thumb_io, name=image.name.replace("products/", ""))
        return thumbnail

    def get_average_rating(self):
        """
        Returns the average of all ratings existing for
        this product in their original value (/100)
        """
        ratings = Rating.objects.filter(product=self).aggregate(
            rating_avg=Avg("rating")
        )
        return (ratings["rating_avg"]) or 0

    def get_average_rating_decimal(self):
        """
        Returns the average of all ratings existing for
        this product out of /5 (for use in star ratings)
        """
        ratings = Rating.objects.filter(product=self).aggregate(
            rating_avg=Avg("rating")
        )
        return self.get_average_rating() / 20

    def get_rating_count(self):
        """
        counts how many ratings completes on this product
        """
        return Rating.objects.filter(product=self).count()

    def get_review_count(self):
        """
        counts how many reviews completes on this product
        """
        return Review.objects.filter(rating__product=self).count()

    def get_product_url(self):
        """
        Creates a redirect url for product
        based on whether products has a set type or not
        """
        url = f"/shop/{self.category.slug}/{self.subcategory.slug}/"
        return (
            url + f"{self.slug}"
            if not self.type
            else url + f"{self.type.slug}/{self.slug}"
        )

    def get_product_code(self):
        """
        Create a random product code for each item
        """
        # Generate a random 4-character string of letters
        first_part = "".join(random.choices(string.ascii_uppercase, k=4))
        # Generate a random 4-digit number
        second_part = "".join(random.choices(string.digits, k=4))
        # Concatenate the two parts with a dash
        product_code = first_part + "-" + second_part
        return product_code


class Rating(models.Model):
    user_id = models.ForeignKey(
        Account, related_name="ratings", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name="ratings", on_delete=models.CASCADE
    )

    class Stars(models.IntegerChoices):
        ONE = 20, "★☆☆☆☆"
        TWO = 40, "★★☆☆☆"
        THREE = 60, "★★★☆☆"
        FOUR = 80, "★★★★☆"
        FIVE = 100, "★★★★★"

    rating = models.IntegerField(choices=Stars.choices)
    date_added = models.DateTimeField(verbose_name="date added", auto_now_add=True)

    class Meta:
        verbose_name_plural = "Ratings"
        ordering = ("date_added", "user_id")

    def __str__(self):
        return f"{self.user_id}: {self.product}"


class Review(models.Model):
    rating = models.ForeignKey(Rating, related_name="reviews", on_delete=models.CASCADE)
    headline = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    date_added = models.DateTimeField(verbose_name="date added", auto_now_add=True)

    class Meta:
        verbose_name_plural = "Reviews"
        ordering = ("date_added",)

    def __str__(self):
        return f"{self.rating.user_id}: {self.headline}"
