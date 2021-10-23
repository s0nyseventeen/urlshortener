from django.shortcuts import render, get_object_or_404
from django.http import (HttpResponse, HttpResponseRedirect,
                         Http404)
from django.views import View
from django.utils import timezone
from .models import ShortUrl
from .forms import UrlForm


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = UrlForm()
        context = {
            'form': form,
        }
        return render(request, 'makeshort/home.html', context)

    def post(self, request, *args, **kwargs):
        form = UrlForm(request.POST)
        template = 'makeshort/home.html'
        context = {
            'form': form,
        }
        if form.is_valid():
            new_url = form.cleaned_data
            obj, created = ShortUrl.objects.get_or_create(url=new_url)
            context = {
                'obj': obj,
                'created': created,
            }
            if created:
                template = 'makeshort/success.html'
            else:
                template = 'makeshort/exists.html'
        return render(request, template, context)


class ShortUrlView(View):
    def get(self, request, short_url=None, *args, **kwargs):
        obj = get_object_or_404(ShortUrl, short_url=short_url)
        qs = ShortUrl.objects.filter(short_url__iexact=short_url)
        delta = timezone.now() - obj.date_created
        if delta.seconds > 3600:  # !!! check this line tmrw
            if not qs.exists():
                raise Http404
        return HttpResponseRedirect(obj.url)
