# Generated by Django 3.2.3 on 2021-05-26 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_alter_feature_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='products.subcategory'),
        ),
    ]
