from django import forms
from .models import Gallery, Invoice, Message, Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    design_image = forms.ImageField(label='Design Idea')


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'


class GallerForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'

    image = forms.ImageField(label='Cake Photo')
