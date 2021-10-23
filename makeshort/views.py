from django.shortcuts import render, get_object_or_404
from django.http import (HttpResponse, HttpResponseRedirect,
                         HttpResponseNotFound)
from django.views import View
from .models import ShortUrl
from django.utils import timezone


def short_url(request, short_url=None, *args, **kwargs):
    obj = get_object_or_404(ShortUrl, short_url=short_url)
    return HttpResponseRedirect(obj.url)


class ShortUrlView(View):
    def get(self, request, short_url=None, *args, **kwargs):
        obj = get_object_or_404(ShortUrl, short_url=short_url)
        delta = timezone.now() - obj.date_created
        if delta.seconds > 3600:
            return HttpResponseNotFound('<h1>Page not found</h1>')
        return HttpResponseRedirect(obj.url)
