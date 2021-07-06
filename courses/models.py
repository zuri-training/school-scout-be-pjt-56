from django.db import models
from school.models import School

# Create your models here.

class Course(models.Model):
    
    PROGRAM_CHOICES = (
    ('phD', 'Doctorate'),
    ('ms', 'Masters'),
    ('bs', 'Bachelors'),
    ('dip', 'Diploma'),
    )

    STUDY_CHOICES = (
    ('fulltime', 'Full Time'),
    ('parttime', 'Part Time'),
    ('both', 'Both'),
    )

    course_name = models.CharField(max_length=200, null=True, blank=True, default='')
    school = models.ForeignKey(School,  related_name='courses', on_delete=models.CASCADE, null=True, blank=True)
    tution_fees = models.IntegerField(null=True, blank=True, default=0)
    requirements = models.CharField(max_length=200, null=True, blank=True, default='')
    program_options = models.CharField(max_length=200, choices=PROGRAM_CHOICES, null=True)
    study_option = models.CharField(max_length=233, choices=STUDY_CHOICES, null=True, blank=True)
    
    def __str__(self):
        return self.course_name
