# Generated by Django 3.2.3 on 2021-06-11 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='street_address1',
            new_name='street_address_1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='street_address2',
            new_name='street_address_2',
        ),
    ]