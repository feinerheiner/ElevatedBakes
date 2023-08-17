"""
URL configuration for elevatedbakes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('add_gallery/', views.create_gallery, name='gallery_form'),
    path('invoice/', views.invoice, name='invoice'),
    path('add_invoice/', views.create_invoice, name='invoice_form'),
    path('contact/', views.contact, name='contact'),
    path('order/', views.create_order, name="order_form"),
    path('message/', views.create_message, name='message_form'),
    path('inbox/', views.inbox, name='inbox'),
    path('gallery/<int:item_id>', views.gallery_detail, name='gallery_detail'),
    path('invoice/<int:item_id>', views.invoice_detail, name='invoice_detail'),
    path('invoice/<int:item_id>/generate-pdf/', views.generate_pdf, name='generate_pdf')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

