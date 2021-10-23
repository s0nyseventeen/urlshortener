from django.db import models
from .utils import create_url


#class ShortUrlManager(models.Manager):
#    def all(self, *args, **kwargs):
#        qs_main = super().all(*args, **kwargs)
#        delta = datetime.now(timezone.utc) - date_created
#        qs = qs_main.filter(date_created=)
#        return qs


class ShortUrl(models.Model):
    url = models.CharField(max_length=255)
    short_url = models.CharField(max_length=6, unique=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)  # when model was created
    updated = models.DateTimeField(auto_now=True)  # changes each time model is updated
    # set_manualy = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        if not self.short_url:  # None or ""
            self.short_url = create_url(self)
        super().save(*args, **kwargs)
