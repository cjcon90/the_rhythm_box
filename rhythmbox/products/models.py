from io import BytesIO
from django.core.files import File
from django.db import models
from PIL import Image
from django.template.defaultfilters import slugify

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

