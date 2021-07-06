from django.db import models

# Create your models here.
class School(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)
    school_name = models.CharField(max_length=200, null=True, blank=True)
    is_affiliated = models.BooleanField(null=True, blank=True, default=True)
    overview = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=235, null=True, blank=True)
    culture = models.CharField(max_length=255, null=True, blank=True)
    #image = models.ImageField(upload_to=None, null=True, blank=True)
    school_ranking =  models.IntegerField(null=True, blank=True)
    website = models.URLField(max_length=234, null=True, blank=True)
    number_of_staff = models.IntegerField(null=True, blank=True)
    telephone = models.CharField(max_length=234, null=True, blank=True)
    mobile = models.CharField(max_length=234, null=True, blank=True)
    email = models.EmailField(max_length=234, blank=True)
    number_of_students = models.IntegerField(null=True, blank=True)
    has_accomodation = models.BooleanField(default=True)
    min_tuition = models.IntegerField(null=True, blank=True)
    max_tuition = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.school_name
