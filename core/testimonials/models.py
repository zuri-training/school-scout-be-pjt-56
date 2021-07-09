from django.db import models


class Testimonial(models.Model):
    
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    author = models.CharField(max_length=5000)
    testimonial = models.TextField(max_length=5000)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.testimonial
        