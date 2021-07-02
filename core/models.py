from django.core import validators
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Testimonial(models.Model):
    testimonial = models.TextField(max_length=5000)

    def __str__(self):
        return self.testimonial 


class UniversityReview(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    university = models.ForeignKey(School, on_delete=models.CASCADE)
    review = models.TextField(max_length=5000)
    rating = models.IntegerField(default=0, 
    
        validators=[
            MaxValueValidator(5), 
            MinValueValidator(0)
            ]
        )

    def __str__(self):
        return self.review
    
