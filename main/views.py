# -*- coding: utf-8 -*-
from django.shortcuts import render


def home(request):
    return render(request, 'main/index.html')


def error_404(request, exception=None):
    return render(request, '404.html', status=404)


def error_500(request):
    return render(request, '500.html', status=500)
