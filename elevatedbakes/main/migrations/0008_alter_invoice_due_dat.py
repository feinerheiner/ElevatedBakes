# Generated by Django 4.2.3 on 2023-08-16 03:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_invoice_delivery_address_invoice_delivery_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='due_dat',
            field=models.DateField(default=datetime.datetime(2023, 9, 14, 21, 44, 40, 563156)),
        ),
    ]
