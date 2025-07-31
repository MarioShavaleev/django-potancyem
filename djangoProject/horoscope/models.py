from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Horoscope(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    peoples = models.TextField(blank=True)
    cost = models.IntegerField(default=0)
    slug = models.SlugField(default='', null=False, db_index=True, unique=True)

    def save(self, *args, **kwargs): #для slug
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super(Horoscope, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('get_info_about_sign_zodiac', args=[self.slug])
