# Generated by Django 3.2.3 on 2021-05-25 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category_friendly_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='friendly_title',
        ),
    ]