# Generated by Django 4.2.3 on 2023-08-14 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_invoice_cake_topper_remove_invoice_deposit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='address2',
            field=models.CharField(max_length=200, null=True),
        ),
    ]