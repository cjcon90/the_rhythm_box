# Generated by Django 4.1.3 on 2023-01-15 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0012_alter_product_thumbnail"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="product_code",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]