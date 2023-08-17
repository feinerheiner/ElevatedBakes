from django.shortcuts import render, redirect
from .models import Gallery, Invoice, Message, Order
from .forms import OrderForm, MessageForm, InvoiceForm, GallerForm
from django.http import HttpResponse
import pdfkit
from django.template import loader
import io
from django.template.loader import render_to_string
from django.utils.text import slugify
import subprocess


# Create your views here.
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Order sent</h1>')
    else:
        form = OrderForm()

    context = {'form': form}

    return render(request, 'main/order_form.html', context)


def create_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Message sent</h1>')
    else:
        form = MessageForm()

    context = {'form': form}

    return render(request, 'main/message_form.html', context)


def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main/invoice_list.html')
    else:
        form = InvoiceForm()
    context = {'form': form}

    return render(request, 'main/invoice_form.html', context)


def create_gallery(request):
    if request.method == 'POST':
        form = GallerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'main/gallery.html')
    else:
        form = GallerForm()
    context = {'form': form}

    return render(request, 'main/gallery_form.html', context)


def home(request):
    return render(request, 'main/home.html')


def invoice(request):
    invoice_list = Invoice.objects.all()
    return render(request, 'main/invoice_list.html', {'invoice_list': invoice_list})


def gallery(request):
    gallery_list = Gallery.objects.all()
    return render(request, 'main/gallery.html', {'gallery_list': gallery_list})


def gallery_detail(request, item_id):
    cake = Gallery.objects.get(pk=item_id)
    return render(request, 'main/gallery_detail.html', {'cake': cake})


def inbox(request):
    messages = Message.objects.all()
    orders = Order.objects.all()
    return render(request, 'main/inbox.html', {'messages': messages, 'orders': orders})


def contact(request):
    return render(request, 'main/contact.html')


def invoice_detail(request, item_id):
    invoice = Invoice.objects.get(pk=item_id)
    return render(request, 'main/invoice_detail.html', {'invoice': invoice})


def generate_pdf(request, item_id):
    invoice = Invoice.objects.get(pk=item_id)
    template = loader.get_template('main/invoice_detail.html')
    html = template.render({'invoice': invoice})
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
    }
    pdf = pdfkit.from_string(html, False, options)
    filename = f'invoice_{item_id}_{slugify(invoice.name)}.pdf'
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{filename}"'

    return response

