# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemap import StaticViewSitemap
from main import views as main_views


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
           '"serviceworker":{"src": "/sw.js"},' \
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
            '{"src":"img/favicon-512x512.png",' \
            '"sizes":"512x512",' \
            '"type":"image/png"}]}'

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('robots.txt', lambda r: HttpResponse(robots, content_type="text/plain")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('manifest.json', lambda r: HttpResponse(manifest, content_type="application/json")),
    path('sw.js', (TemplateView.as_view(template_name="sw.js", content_type='application/javascript', )), name='sw.js'),
]

handler404 = main_views.error_404
handler500 = main_views.error_500