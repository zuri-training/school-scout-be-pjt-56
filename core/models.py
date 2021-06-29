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


class Comment(models.Model): # Create new course model

    article = models.ForeignKey(Article, related_name="comment", on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return '%s - %s' % (self.article, self.commenter)


#dummy content
class School(models.Model): # Create new school model
   
    name = models.CharField(max_length=150, help_text='Enter Name of School', blank=False, unique=True)
    overview = models.TextField()
    website = models.URLField(max_length=250, help_text='Enter scholarship application website', blank=False, unique=True) 

    def __str__(self):
        return "{}".format(self.name)


#dummy content
class Course(models.Model): # Create new course model
   
    name = models.CharField(max_length=150, help_text='Enter Name of course', blank=False, unique=True)
    institution = models.ForeignKey(School, on_delete=models.CASCADE)
    requirements = models.TextField()

    def __str__(self):
        return "{}".format(self.name)


#options for scholarship class
FUNDING_CHOICES = (
    ('CHOOSE', '.....'),
    ('PARTIAL', 'Partial funding'),
    ('FULL', 'Fully funded'),
)

DEGREE = (
    ('CHOOSE', '.....'),
    ('UNDERGRADUATE', 'Undergraduates only'),
    ('MASTERS', 'Masters only'),
    ('DOCTORATE', 'PhD only'),
    ('ALL', 'All degrees'),
)
class Scholarship(models.Model): # Create new scholarship model
   
    name = models.CharField(max_length=150, help_text='Enter Name of Scholarship', blank=False, unique=True)
    donor = models.CharField(max_length=150, help_text='Enter Name of Scholarship Donor', blank=True)
    description = models.TextField()
    #slug = models.SlugField(unique=True)
    institution = models.ForeignKey(School, default=1, on_delete=models.CASCADE)
    course_name = models.ForeignKey(Course, default=1, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    funding = models.CharField(max_length=15, choices=FUNDING_CHOICES, verbose_name=('Type of funding'), default='.....')
    degree_level = models.CharField(max_length=30, choices=DEGREE, default='.....')
    amount = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    deadline = models.DateTimeField(auto_now_add=True, verbose_name=('Application deadline'))
    requirements = models.TextField(verbose_name=('Application requirements')) 
    date_published = models.DateTimeField(auto_now_add=True)
    contact = models.CharField(max_length=250, help_text='Enter full name of Contact person')
    telephone = PhoneNumberField(help_text='Enter phone number of Contact person')
    email = models.EmailField(max_length=200, help_text='Enter email of Contact person', blank=False, unique=True)
    website = models.URLField(max_length=250, help_text='Enter scholarship application website', blank=False, unique=True)  

    class Meta:
        ordering = ['-date_published']

    def __str__(self):
        return "{}".format(self.name)