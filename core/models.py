from django.conf import settings
from django.db import models
from django.contrib.auth.models import User  # import the superuser
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Article(models.Model): # Create new post model

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=False, unique=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

       
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return "{}".format(self.title)

    def get_absolute_url(self):
        kwargs = {
            'pk' : self.id,
            'slug': self.slug
        }
        return reverse('article_detail', kwargs=kwargs)
    
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)