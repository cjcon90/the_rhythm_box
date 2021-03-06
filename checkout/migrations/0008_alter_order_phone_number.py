# Generated by Django 3.2.3 on 2021-06-13 19:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_auto_20210613_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='This is not a valid phone number', regex='^(\\+\\d{1,2}\\s)?\\(?\\d{3}\\)?[\\s.-]\\d{3}[\\s.-]\\d{4}$')]),
        ),
    ]
