# Generated by Django 4.2.3 on 2023-08-14 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_message_phone_alter_order_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='cake_topper',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='deposit',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='other',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='setup',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='subtotal',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='total',
        ),
        migrations.AddField(
            model_name='invoice',
            name='cake_topper_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='filling_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='other_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='other_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='setup_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='address2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='delivery_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='tax',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
    ]
