# Generated by Django 4.2.3 on 2023-08-16 14:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_invoice_delivery_address_alter_invoice_due_dat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='due_dat',
        ),
        migrations.AddField(
            model_name='invoice',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 15, 8, 5, 46, 232729)),
        ),
    ]
