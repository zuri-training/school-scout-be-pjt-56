from django.contrib import admin
from .models import Article, Comment, Course, Scholarship, School


# Register your models here.

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Scholarship)
admin.site.register(School)
admin.site.register(Course)