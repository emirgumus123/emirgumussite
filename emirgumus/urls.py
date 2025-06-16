"""
URL configuration for emirgumus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from website.views import anasayfa , haber_detay , hakkimizda , haber_listesi , hizmetler , hizmet_detay , iletisim

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', anasayfa, name='anasayfa'),
    path('haber/<int:haber_id>/', haber_detay, name='haber_detay'),
    path('hakkimizda/', hakkimizda, name='hakkimizda'),
    path('haberler/', haber_listesi, name='haber_listesi'),
    path('hizmetler/', hizmetler, name='hizmetler'),
    path('hizmet/<int:pk>/', hizmet_detay, name='hizmet_detay'),
    path('iletisim/', iletisim, name='iletisim'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
