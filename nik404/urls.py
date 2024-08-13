"""
URL configuration for nik404 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from azbankgateways.urls import az_bank_gateways_urls
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('website.urls')),
    path('blog/',include('blog.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('accounts.urls')),
    path('pythonium/', include('pythonium.urls')),
    path('cart/', include('cart.urls')),
    # path("bankgateways/", az_bank_gateways_urls()),
    path('payment/', include('payment.urls')),
]
    
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom 404 error view
handler404 = 'website.views.error_404' 
# Custom 500 error view
handler500 = 'website.views.error_500' 
# Custom 403 error view
handler403 = 'website.views.error_403'