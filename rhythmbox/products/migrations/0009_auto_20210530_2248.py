# Generated by Django 3.2.3 on 2021-05-30 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_rating_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='products.subcategory'),
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(max_length=500),
        ),
    ]
