from django.db import models
from django.contrib.auth.models import User  # import the superuser


from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Article(models.Model): # Create new post model

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=False, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return "{}".format(self.title)


