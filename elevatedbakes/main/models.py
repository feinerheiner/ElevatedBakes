from django.db import models
from decimal import Decimal, ROUND_HALF_UP
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime, timedelta


# Create your models here.
class Gallery(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='gallery/')


class Invoice(models.Model):
    def __str__(self):
        return f"Invoice #{self.pk} - {self.date}"

    DELIVERY_CHOICES = [
        ('Picked up', 'Picked up'),
        ('Regular', 'Regular'),
        ('Extended', 'Extended'),
    ]

    date = models.DateField(auto_now_add=True, blank=True)
    name = models.CharField(max_length=100)
    phone = PhoneNumberField(default='+1')
    email = models.EmailField()
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)
    due_date = models.DateField(default=datetime.now() + timedelta(days=30))
    paid = models.BooleanField(default=False)
    delivery_address = models.CharField(max_length=200, default=' ', null=True, blank=True)
    delivery_city = models.CharField(max_length=100, default=' ', null=True, blank=True)
    delivery_state = models.CharField(max_length=2, default=' ', null=True, blank=True)
    delivery_zip = models.CharField(max_length=10, default=' ', null=True, blank=True)
    cake_flavor = models.CharField(max_length=100)
    filling_flavor = models.CharField(max_length=100)
    delivery_type = models.CharField(max_length=100, choices=DELIVERY_CHOICES)
    delivery_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0.00)
    setup_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0.00)
    cake_topper_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0.00)
    cake_cost = models.DecimalField(max_digits=10, decimal_places=2)
    filling_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0.00)
    other_description = models.TextField(null=True, blank=True)
    other_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0.00)
    tax = models.DecimalField(max_digits=4, decimal_places=2)  # This needs to be stored as a percent

    def subtotal(self):
        return self.delivery_cost + self.setup_cost + self.cake_topper_cost + self.cake_cost + self.filling_cost + \
            self.other_cost

    def calculatedTax(self):
        subtotal = self.subtotal()
        tax = subtotal * (self.tax / 100)
        return tax.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)

    def total(self):
        subtotal = self.subtotal()
        tax = self.calculatedTax()
        total = subtotal + tax
        return total.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)

    def deposit(self):
        total = self.total()
        deposit = total * Decimal(.5)
        return deposit.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)


class Message(models.Model):
    def __str__(self):
        return f"{self.name} - {self.date}"

    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100)
    phone = PhoneNumberField(default='+1')
    email = models.EmailField()
    message = models.TextField()


class Order(models.Model):
    def __str__(self):
        return f"Order #{self.pk} - {self.name} - {self.date}"

    EVENT_CHOICES = [
        ('Birthday', 'Birthday'),
        ('Wedding', 'Wedding'),
        ('Celebration', 'Celebration'),
        ('I want cake', 'I want cake'),
    ]

    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100)
    phone = PhoneNumberField(default='+1')
    email = models.EmailField()
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)
    event_type = models.CharField(max_length=100, choices=EVENT_CHOICES)
    event_date = models.DateField()
    cake_flavor = models.CharField(max_length=100)
    filling_flavor = models.CharField(max_length=100)
    servings = models.CharField(max_length=3)
    design = models.TextField()
    message = models.TextField()
    design_image = models.ImageField(upload_to='orders/')





