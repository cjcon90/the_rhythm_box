from io import BytesIO
from django.core.files import File
from django.db import models
from django.db.models import Avg
from PIL import Image
from django.template.defaultfilters import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import Account

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('ordering','title')
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Subcategory(models.Model):
    parent = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Subcategories'
        ordering = ('parent', 'ordering','title')
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Type(models.Model):
    parent = models.ForeignKey(Subcategory, related_name='types', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Types'
        ordering = ('parent', 'ordering','title')
    
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
        verbose_name_plural = 'Brands'
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, related_name='subcategory', blank=True, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, related_name='type', null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    brand = models.ForeignKey('Brand', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.IntegerField(default=15)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="products/", blank=True, null=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.thumbnail = self.make_thumbnail(self.image)
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def make_thumbnail(self, image, size=(300,200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)
        return thumbnail

    def average_rating(self):
        reviews = Review.objects.filter(product=self).aggregate(rating_avg=Avg('rating'))
        return (reviews['rating_avg'])


class Review(models.Model):
    author = models.ForeignKey(Account, related_name='reviews', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    date_added = models.DateTimeField(verbose_name='date added', auto_now_add=True)
    rating = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)])
    headline = models.CharField(max_length=50, blank=False)
    content = models.TextField()

    class Meta:
        verbose_name_plural = 'Reviews'
        ordering = ('date_added','author')
    
    def __str__(self):
        return f"{self.author}: {self.product}"

    def save(self, *args, **kwargs):
        self.rating = self.rating * 20
        super().save(*args, **kwargs)