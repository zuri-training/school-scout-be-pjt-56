from core.department.models import Department
from django.db import models
from autoslug import AutoSlugField
from core.schools.models import School


#User = get_user_model()


"""COURSE MODEL"""
class Course(models.Model):

    OPTIONS = [
        ("nil", "....."),
        ("Undergraduate", "Undergraduate"),
        ("Postgraduate", "Postgraduate"),
        ("Doctorate", "Doctorate"),
    ]
   
    course_name = models.CharField(max_length=200, null=True, blank=True, default='')
    slug = AutoSlugField(populate_from='course_name', blank=True, editable=True)
    school_name = models.ForeignKey(School, related_name='courses', on_delete=models.CASCADE, null=True, blank=True)
    image = models.FileField(upload_to=None, null=True, blank=True)
    tution_fees = models.CharField(max_length=200, null=True, blank=True, default='')
    course_requirements = models.TextField()
    program = models.CharField(max_length=200, choices=OPTIONS, default='.....', blank=False)
    name_of_department = models.ForeignKey(Department, related_name="department", on_delete=models.CASCADE)
    school_location = models.CharField(max_length=200, null=True, blank=True, default='')
    duration = models.CharField(max_length=200, null=True, blank=True, default='')
    bookmarkIcon = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.course_name
