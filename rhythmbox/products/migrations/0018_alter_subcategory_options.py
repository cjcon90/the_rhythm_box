# Generated by Django 3.2.3 on 2021-05-26 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20210525_2340'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ('parent', 'title'), 'verbose_name_plural': 'Subcategories'},
        ),
    ]
