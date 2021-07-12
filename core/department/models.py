
from core.faculty.models import Faculty
from django.db import models
from autoslug import AutoSlugField



"""DEPARTMENT MODEL""" 
class Department(models.Model): # Create new department model

    name = models.CharField(max_length=150, help_text='Enter Department name', blank=False, unique=True)
    slug = AutoSlugField(populate_from='name', blank=True, editable=True)
    faculty = models.ForeignKey(Faculty, related_name="faculty", on_delete=models.CASCADE)
    
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return "{}".format(self.name)
