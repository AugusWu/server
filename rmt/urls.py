"""rmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from ruimu.admin import site
from . import settings

urlpatterns = [
    url(r'^adminrmt/', include(site.urls)),
    url(r'^$', 'ruimu.views.home_view'),
    url(r'^product/(?P<id>\d+)/$', 'ruimu.views.product_detail'),
    url(r'^product$', 'ruimu.views.product_view'),
    url(r'^brand$', 'ruimu.views.brand_view'),
    url(r'^brand/(?P<id>\d+)/$', 'ruimu.views.brand_detail', name='brand_detail'),
    url(r'^about$', 'ruimu.views.about_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
