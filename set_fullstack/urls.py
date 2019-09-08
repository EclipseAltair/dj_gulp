# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.contrib.sitemaps.views import sitemap
from .sitemap import StaticViewSitemap


robots = 'User-agent: *\n' \
         'Disallow: /admin\n' \
         'Sitemap: http://site.site/sitemap.xml'

sitemaps = {
    'static': StaticViewSitemap,
    }

manifest = '{"name":"",' \
           '"short_name":"",' \
           '"start_url":"/",' \
           '"display":"standalone",' \
           '"theme_color":"#000",' \
           '"background_color":"#000",' \
           '"description":"",' \
           '"icons":' \
            '[{"src":"img/favicon-16x16.png",' \
            '"sizes":"16x16",' \
            '"type":"image/png"},' \
            '{"src":"img/favicon-32x32.png",' \
            '"sizes":"32x32",' \
            '"type":"image/png"},' \
            '{"src":"img/favicon-196x196.png",' \
            '"sizes":"196x196",' \
            '"type":"image/png"},' \
            '{"src":"img/favicon-196x196.png",' \
            '"sizes":"512x512",' \
            '"type":"image/png"}]}'

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('robots.txt', lambda r: HttpResponse(robots, content_type="text/plain")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('manifest.json', lambda r: HttpResponse(manifest, content_type="application/json"))

] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)