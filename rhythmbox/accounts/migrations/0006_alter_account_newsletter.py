# Generated by Django 3.2.3 on 2021-06-20 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_newslettersub_subscription_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='newsletter',
            field=models.BooleanField(default=True),
        ),
    ]
