from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import Account
from products.models import Product

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
