# -*- coding: utf-8 -*-
from django.urls import path
from django.http import HttpResponse
from django.contrib.sitemaps.views import sitemap
from . import views
from .sitemap import StaticViewSitemap


sitemaps = {
    'static': StaticViewSitemap,
    }

urlpatterns = [
    path('', views.home, name='home'),
    path('robots.txt', lambda r: HttpResponse("User-agent: *\nDisallow: /admin", content_type="text/plain")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('manifest.json', lambda r: HttpResponse('{"name": "","short_name": "","start_url": "/",'
                                                 '"display": "standalone","theme_color": "", "background_color": ""}', content_type="application/json"))
]